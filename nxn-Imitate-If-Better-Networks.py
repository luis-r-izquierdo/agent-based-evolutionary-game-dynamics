#%%
import mesa
from mesa.space import NetworkGrid
import networkx as nx
import seaborn as sns
from matplotlib import pyplot as plt
import math
import numpy as np
import random
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

payoffs_default = {
    'A': {'A': (1, 1), 'B': (0, 0)},
    'B': {'A': (0, 0), 'B': (2, 2)}
}

class nxnImitationModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n, seed=None, network_type="wheel_network",prob_revision=0.1,payoffs=payoffs_default,initial_probs=None,edges=1,avg_degree=4,prob_rewire=0.3,noise=0.1,prob_link=0.5):

        super().__init__(seed=seed)
        self.num_agents = n
        self.running = True
        self.prob_revision = prob_revision
        self.initial_probs = initial_probs
        self.payoffs=payoffs
        self.edges=edges
        self.avg_degree=avg_degree
        self.prob_rewire=prob_rewire
        self.noise=noise
        self.prob_link=prob_link
        self.grid=Network(n, network_type,edges,avg_degree,prob_rewire,prob_link)

        assert len(self.grid.G.nodes) == self.num_agents, f"Mismatch: {len(self.grid.G.nodes)} nodi vs {self.num_agents} agenti"
        

        # Create agents
        agents = nxnImitationAgent.create_agents(model=self, n=n)

        for node, agent in zip(self.grid.G.nodes, agents):
            print(f"Posizionamento agente {agent} nel nodo {node} con strategia {agent.strategy}")
            self.grid.place_agent(agent, node)

        self.datacollector = mesa.DataCollector(
            agent_reporters={
                "Strategy": "strategy",
                "Payoff": "payoff",
                "Wealth": "wealth",
            }
            )

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("update_strategy")

class nxnImitationAgent(mesa.Agent):
        
    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1
        self.steps_not_given = 0
        self.strategy_after_revision = None
        self.payoffs=model.payoffs
        self.wealth = 1
        self.initial_probs = model.initial_probs

        strategies=list(self.payoffs.keys())

        if self.initial_probs is None:
            self.initial_probs = [1/len(strategies)] * len(strategies)

        self.strategy = self.random.choices(strategies,weights=self.initial_probs,k=1)[0]

    def update_payoff(self):
        neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
        if len(neighbors) > 0:
            for other in neighbors:
                # Calcola i payoff in base alle strategie correnti
                payoff_self, payoff_other = self.payoffs[self.strategy][other.strategy]
                
                # Aggiungi il payoff a entrambi gli agenti
                self.wealth = payoff_self
                other.wealth = payoff_other

    def update_strategy(self):
        if self.random.random() < self.model.prob_revision:  # L'agente può aggiornare la strategia
            strategies = list(self.payoffs.keys())

            # 1. Con probabilità "noise", cambia a una strategia casuale
            if self.random.random() < self.model.noise:
                self.strategy = self.random.choice(strategies)

            # 2. Altrimenti, imita un vicino migliore
            else:
                neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
                if len(neighbors) > 0:
                    other = self.random.choice(neighbors)
                    if other.wealth > self.wealth:
                        self.strategy = other.strategy


class Network(NetworkGrid):

    def __init__(self, num_nodes, network_model_type,edges,avg_degree,prob_rewire,prob_link):
        self.num_nodes = num_nodes
        self.network_model_type = network_model_type
        self.edges=edges
        self.avg_degree=avg_degree
        self.prob_rewire=prob_rewire
        self.prob_link=prob_link

        super().__init__(self.build_network())  # Passa la rete costruita al NetworkGrid
    
    def build_network(self):
        """Costruisce una rete in base al tipo di modello"""
        # Usa un dizionario per mappare il modello alla funzione
        model_functions = {
            "erdos_renyi": self.erdos_renyi,
            "watts_strogatz": self.watts_strogatz,
            "preferential_attachment": self.preferential_attachment,
            "ring_network": self.ring_network,
            "star_network": self.star_network,
            "grid_4_neighbors": self.grid_4_neighbors,
            "wheel_network": self.wheel_network,
            "path_network": self.path_network
        }
        
        if self.network_model_type in model_functions:
            graph=model_functions[self.network_model_type](self.num_nodes)
            self.pos=nx.spring_layout(graph)
            return graph
        else:
            raise ValueError("Unknown network model type: {}".format(self.network_model_type))

    def erdos_renyi(self, num_nodes):
        """Crea un grafo Erdős–Rényi"""
        graph = nx.erdos_renyi_graph(n=num_nodes, p=self.prob_link)
        nx.draw(graph, with_labels=True)
        #plt.show()
        return graph
    
    def watts_strogatz(self, num_nodes):
        """Crea un grafo di Watts-Strogatz"""
        graph = nx.watts_strogatz_graph(n=num_nodes, k=self.avg_degree, p=self.prob_rewire)
        nx.draw(graph, with_labels=True)
        #plt.show()
        return graph
    
    def preferential_attachment(self, num_nodes):
        """Crea un grafo di attaccamento preferenziale"""
        graph = nx.barabasi_albert_graph(n=num_nodes, m=self.edges)
        nx.draw(graph, with_labels=True)
        #plt.show()
        return graph
    
    def ring_network(self, num_nodes):
        """Crea un grafo ad anello"""
        graph = nx.cycle_graph(n=num_nodes)
        nx.draw(graph, with_labels=True)
        #plt.show()
        return graph
    
    def star_network(self, num_nodes):
        """Crea un grafo a stella"""
        graph = nx.star_graph(n=num_nodes-1)
        nx.draw(graph, with_labels=True)
        #plt.show()
        return graph
    
    def grid_4_neighbors(self, num_nodes):
        side = int(math.ceil(math.sqrt(num_nodes)))  # usa ceil invece di floor
        graph = nx.grid_2d_graph(side, side, periodic=False)
        # Può contenere più nodi di quelli richiesti, ma possiamo prenderne solo n dopo
        sub_nodes = list(graph.nodes)[:num_nodes]
        subgraph = graph.subgraph(sub_nodes).copy()
        pos = {node: (node[0], node[1]) for node in subgraph.nodes()}
        nx.draw(subgraph, pos, with_labels=True)
        #plt.show()
        return subgraph

    
    def wheel_network(self, num_nodes):
        """Crea un grafo a ruota"""
        graph = nx.wheel_graph(n=num_nodes)
        nx.draw(graph, with_labels=True)
        #plt.show()
        return graph
    
    def path_network(self, num_nodes):
        """Crea una rete a percorso"""
        graph = nx.cycle_graph(num_nodes)
        edges = list(graph.edges)
        random_edge = random.choice(edges)
        graph.remove_edge(*random_edge)
        nx.draw(graph, with_labels=True)
        #plt.show()
        return graph

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulazione Strategica")
        self.strategy_colors = None  # Colori assegnati alle strategie

        self.num_agents = tk.IntVar(value=100)
        self.network_type = tk.StringVar(value="erdos_renyi")
        self.steps = tk.IntVar(value=50)
        self.prob_revision = tk.DoubleVar(value=0.1)
        self.payoffs_input = tk.StringVar(value=str(payoffs_default))
        self.initial_distribution = tk.StringVar(value="None")
        self.edges = tk.IntVar(value=1)
        self.noise = tk.DoubleVar(value=0.1)
        self.avg_degree = tk.IntVar(value=4)
        self.prob_rewiring = tk.DoubleVar(value=0.3)
        self.prob_link = tk.DoubleVar(value=0.5)
        self.show_animation = tk.BooleanVar(value=True)  # Default: mostra animazione

        self.frame_canvas = ttk.Frame(self.root)
        self.frame_canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True) 

        # Canvas dei grafici
        self.figure = plt.Figure(figsize=(8, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame_canvas)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Canvas della rete
        self.network_figure = plt.Figure(figsize=(8, 4), dpi=100)
        self.network_canvas = FigureCanvasTkAgg(self.network_figure, master=self.frame_canvas)
        self.network_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        self.setup_widgets()

    def setup_widgets(self):
        control_frame = ttk.Frame(self.root)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Label(control_frame, text="Numero Agenti").pack()
        ttk.Entry(control_frame, textvariable=self.num_agents).pack()

        ttk.Label(control_frame, text="Tipo di Rete").pack()
        ttk.OptionMenu(control_frame, self.network_type, "erdos_renyi","watts_strogatz", "preferential_attachment", "ring_network","star_network","grid_4_neighbors","wheel_network","path_network","erdos_renyi").pack()

        ttk.Label(control_frame, text="Passi di simulazione").pack()
        ttk.Entry(control_frame, textvariable=self.steps).pack()

        ttk.Label(control_frame, text="Probabilità di Revisione").pack()
        ttk.Entry(control_frame, textvariable=self.prob_revision).pack()

        ttk.Label(control_frame, text="Rumore").pack()
        ttk.Entry(control_frame, textvariable=self.noise).pack()

        ttk.Label(control_frame, text="Distribuzione iniziale").pack()
        ttk.Entry(control_frame, textvariable=self.initial_distribution).pack()

        ttk.Label(control_frame, text="Per Erdos ").pack()
        ttk.Entry(control_frame, textvariable=self.prob_link).pack()

        ttk.Label(control_frame, text="Per preferential attachment").pack()
        ttk.Label(control_frame, text="Scegli il grado").pack()
        ttk.Entry(control_frame, textvariable=self.edges).pack()

        ttk.Label(control_frame, text="Per small-world network").pack()
        ttk.Label(control_frame, text="Grado medio").pack()
        ttk.Entry(control_frame, textvariable=self.avg_degree).pack()
        ttk.Label(control_frame, text="Probabilità rewiring").pack()
        ttk.Entry(control_frame, textvariable=self.prob_rewiring).pack()

        ttk.Label(control_frame, text="Matrice dei Payoff (formato dizionario)").pack()
        self.payoffs_text = tk.Text(control_frame, height=6, width=50)
        self.payoffs_text.pack()
        self.payoffs_text.insert("1.0", str(payoffs_default))  # Inserisce il dizionario iniziale

        ttk.Checkbutton(control_frame, text="Mostra Animazioni", variable=self.show_animation).pack()
        ttk.Button(control_frame, text="Esegui Simulazione", command=self.run_simulation).pack(pady=10)


    def run_simulation(self):

        payoffs = eval(self.payoffs_text.get("1.0", tk.END))

        model = nxnImitationModel(
            n=self.num_agents.get(),
            network_type=self.network_type.get(),
            prob_revision=self.prob_revision.get(),
            payoffs=payoffs,
            edges=self.edges.get(),
            avg_degree=self.avg_degree.get(),
            prob_rewire=self.prob_rewiring.get(),
            noise=self.noise.get(),
            prob_link=self.prob_link.get(),
            initial_probs=eval(self.initial_distribution.get()) if self.initial_distribution.get() != "None" else None
        )

        print(f"[INFO] Numero nodi: {len(model.grid.G.nodes)}")
        print(f"[INFO] Numero agenti: {len(model.agents)}")


        for _ in range(self.steps.get()):
            model.step()


        # Prepara i dati per l’animazione
        agent_data = model.datacollector.get_agent_vars_dataframe()
        strategy_snapshots_df = agent_data['Strategy'].unstack()
        # Crea un mapping: agent_id -> agent_pos (la tupla)
        id_to_pos = {agent.unique_id: agent.pos for agent in model.agents}

        strategy_snapshots = []
        for step in strategy_snapshots_df.index:
            snapshot_raw = strategy_snapshots_df.loc[step].to_dict()
            # Rimpiazza gli ID con le posizioni nei dizionari snapshot
            snapshot = {id_to_pos[agent_id]: strategy for agent_id, strategy in snapshot_raw.items()}
            strategy_snapshots.append(snapshot)


        # Distribuzione strategie nel tempo (dataframe: step x strategie)
        strategy_counts = strategy_snapshots_df.apply(lambda x: x.value_counts(normalize=True), axis=1).fillna(0)


        if self.show_animation.get():
            self.strategy_colors = self.animate_network(model.grid.G, model.grid.pos, strategy_snapshots)
            self.animate_strategy_distribution_stackplot(strategy_counts, self.strategy_colors)
        else:
            all_strategies = strategy_counts.columns
            cmap_name = 'tab10' if len(all_strategies) <= 10 else 'tab20'
            color_palette = plt.cm.get_cmap(cmap_name, len(all_strategies))
            self.strategy_colors = {strategy: color_palette(i) for i, strategy in enumerate(all_strategies)}
            self.plot_strategy_distribution(model)
            self.plot_network(model.grid.G,model.grid.pos,model=model, strategy_colors=self.strategy_colors)

    def plot_network(self, graph, pos, model=None, strategy_colors=None):
        self.network_figure.clf()
        ax = self.network_figure.add_subplot(111)
        ax.set_title("Rete degli Agenti")

        # Se abbiamo un modello e la mappa dei colori, coloriamo in base alla strategia
        if model and strategy_colors:
            # Costruisci lista dei colori per i nodi in base alla strategia corrente degli agenti
            node_colors = []
            for node in graph.nodes:
                agents = model.grid.get_cell_list_contents([node])
                if agents:
                    strategy = agents[0].strategy
                    color = strategy_colors.get(strategy, 'gray')
                else:
                    color = 'gray'
                node_colors.append(color)
        else:
            node_colors = 'lightblue'

        nx.draw(graph, pos, with_labels=True, node_color=node_colors, edge_color='gray', ax=ax)
        self.network_canvas.draw()

    def animate_network(self, graph, pos, strategy_snapshots):
        self.network_figure.clf()
        ax = self.network_figure.add_subplot(111)
        ax.set_title("Evoluzione delle Strategie")

        # Crea palette di colori dinamicamente
        all_strategies = sorted({s for snapshot in strategy_snapshots for s in snapshot.values()})
        cmap_name = 'tab10' if len(all_strategies) <= 10 else 'tab20'
        color_palette = plt.cm.get_cmap(cmap_name, len(all_strategies))
        strategy_colors = {strategy: color_palette(i) for i, strategy in enumerate(all_strategies)}

        def update(frame):
            ax.clear()
            ax.set_title(f"Passo {frame + 1}")
            snapshot = strategy_snapshots[frame]
            node_colors = [strategy_colors.get(snapshot.get(node, 'gray'), 'gray') for node in graph.nodes]
            nx.draw(graph, pos, node_color=node_colors, edge_color='gray', ax=ax, with_labels=False, node_size=80)

            # DEBUG: Stampa le strategie per ogni nodo
            for node in graph.nodes:
                strategy = snapshot.get(node)
                if strategy is None:
                    print(f"[DEBUG] Nodo {node} senza strategia al frame {frame + 1}")
                else:
                    print(f"[DEBUG] Nodo {node} ha strategia {strategy} al frame {frame + 1}")

        anim = FuncAnimation(self.network_figure, update, frames=len(strategy_snapshots), interval=300, repeat=False)
        self.network_canvas.draw()

        return strategy_colors
    
    def animate_strategy_distribution_stackplot(self, strategy_counts, strategy_colors):
        self.figure.clf()
        ax = self.figure.add_subplot(111)
        ax.set_title("Distribuzione Strategie (Stacked Area)")

        strategies = list(strategy_counts.columns)
        colors = [strategy_colors.get(s, 'gray') for s in strategies]

        def update(frame):
            ax.clear()
            ax.set_title(f"Distribuzione Strategie - Passo {frame + 1}")
            ax.set_ylim(0, 1)
            # Crea lo stackplot con dati fino al frame corrente
            x_vals = list(range(frame + 1))
            y_vals = [strategy_counts[s].iloc[:frame + 1].values for s in strategies]
            ax.stackplot(x_vals, *y_vals, labels=strategies, colors=colors)
            ax.set_xlabel("Passo della Simulazione")
            ax.set_ylabel("Frequenza")
            ax.legend(loc="upper right")
            ax.grid(True)

        anim = FuncAnimation(self.figure, update, frames=len(strategy_counts), interval=300, repeat=False)
        self.canvas.draw()



    def plot_strategy_distribution(self, model):
        # Pulisci la figura corrente prima di disegnare
        self.figure.clf()

        # Ottieni i dati
        agent_data = model.datacollector.get_agent_vars_dataframe()
        strategy_counts = agent_data['Strategy'].unstack().apply(lambda x: x.value_counts(normalize=True), axis=1).fillna(0)
        wealth_history = agent_data['Wealth'].unstack().mean(axis=1)


        # Subplot 3: Area plot (stackplot)
        ax3 = self.figure.add_subplot(111)
        strategies = strategy_counts.columns
        colors = [self.strategy_colors.get(s, 'gray') for s in strategies]
        ax3.stackplot(strategy_counts.index,
                    *[strategy_counts[s] for s in strategies],
                    labels=strategies,
                    colors=colors)
        ax3.set_title("Distribuzione Strategie (Stacked Area)")
        ax3.set_xlabel("Passo della Simulazione")
        ax3.set_ylabel("Frequenza")
        ax3.legend(loc='upper right')
        ax3.grid(False)

        self.figure.tight_layout()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
