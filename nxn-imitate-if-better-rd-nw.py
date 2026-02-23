import random                             # Per operazioni di casualità
import networkx as nx                     # Per creare e gestire grafi
import matplotlib.pyplot as plt           # Per visualizzare grafici
import numpy as np                        # Per operazioni matematiche
from mesa import Agent, Model             # Componenti base del framework Mesa
from mesa.time import SimultaneousActivation  # Scheduler simultaneo degli agenti
from mesa.space import NetworkGrid        # Spazio di simulazione basato su grafo
from mesa.datacollection import DataCollector  # Raccolta dati da agenti/modello
import pandas as pd                       # Per manipolare e salvare i dati

# ---- DEFINIZIONE DELL'AGENTE ----
class PlayerAgent(Agent):
    def __init__(self, unique_id, model, strategy):
        super().__init__(unique_id, model)   # Inizializzazione dell'agente con ID univoco e modello
        self.strategy = strategy   # Strategia attuale dell'agente ('A' o 'B')
        self.payoff = 0            # Ricompensa accumulata nell'interazione con altri agenti

    def play_game(self):
        self.payoff = 0  # Reset della ricompensa prima di ogni gioco
        neighbor_ids = self.model.grid.get_neighbors(self.pos, include_center=False)  # Trova i vicini dell'agente
        for neighbor_id in neighbor_ids:  # Per ogni vicino
            neighbors = self.model.grid.get_cell_list_contents([neighbor_id])  # Ottiene l'agente vicino
            if not neighbors:
                continue
            neighbor = neighbors[0]  # Se l'agente vicino esiste
            payoff_self, _ = self.model.game(self.strategy, neighbor.strategy)  # Calcola il payoff dell'interazione
            self.payoff += payoff_self  # Aggiunge il payoff ottenuto dall'interazione al totale

    def update_strategy(self):
        # Se una probabilità casuale è maggiore della probabilità di revisione, non si aggiorna la strategia
        if random.random() > self.model.prob_revision:
            return

        # Con una certa probabilità "di rumore", l'agente sceglie una strategia casuale
        if random.random() < self.model.noise:
            self.strategy = random.choice(self.model.strategies)  # Sceglie una strategia casuale
            return

        # Altrimenti, copia la strategia del vicino che ha il miglior payoff
        neighbor_ids = self.model.grid.get_neighbors(self.pos, include_center=False)  # Trova i vicini
        if not neighbor_ids:
            return
        neighbor_id = random.choice(neighbor_ids)  # Seleziona un vicino casualmente
        neighbors = self.model.grid.get_cell_list_contents([neighbor_id])  # Ottiene il vicino selezionato
        if not neighbors:
            return
        neighbor = neighbors[0]
        if neighbor.payoff > self.payoff:  # Se il vicino ha un payoff maggiore
            self.strategy = neighbor.strategy  # Adotta la strategia del vicino

    def step(self):
        # Fase del ciclo in cui l'agente gioca e poi aggiorna la sua strategia
        self.play_game()  # L'agente gioca una partita con i suoi vicini
        self.update_strategy()  # L'agente aggiorna la sua strategia in base alle interazioni

# ---- DEFINIZIONE DEL MODELLO ----
class NXNModel(Model):
    def __init__(self, N=100):
        self.num_agents = N                         # Numero di agenti nel modello
        self.strategies = ['A', 'B']                # Strategie disponibili ('A' o 'B')
        self.prob_revision = 0.10                   # Probabilità che un agente decida di aggiornare la propria strategia
        self.noise = 0.03                           # Probabilità che un agente scelga una strategia casuale (errore)
        self.schedule = SimultaneousActivation(self)  # Scheduler che gestisce l'attivazione simultanea degli agenti
        self.G = nx.erdos_renyi_graph(n=N, p=0.1)   # Crea un grafo casuale con N nodi e probabilità p per ogni arco
        self.grid = NetworkGrid(self.G)             # Spazio di simulazione basato sul grafo

        # Inizializzazione delle strategie degli agenti (70% A, 30% B)
        initial_strategies = ['A'] * 70 + ['B'] * 30
        random.shuffle(initial_strategies)

        # Creazione e posizionamento degli agenti sulla rete
        for i in range(self.num_agents):
            strategy = initial_strategies[i]  # Assegna una strategia casuale all'agente
            agent = PlayerAgent(i, self, strategy)  # Crea l'agente con una strategia
            self.schedule.add(agent)  # Aggiungi l'agente allo scheduler
            self.grid.place_agent(agent, i)  # Posiziona l'agente nel grafo
            agent.pos = i  # Salva la posizione dell'agente nel grafo

        # Calcola la disposizione iniziale per il disegno del grafo
        self.pos = nx.spring_layout(self.G, seed=42)

        # Crea un DataCollector per raccogliere dati sulle strategie degli agenti
        self.datacollector = DataCollector(
            model_reporters={
                "Count_A": lambda m: sum(1 for a in m.schedule.agents if a.strategy == 'A'),
                "Count_B": lambda m: sum(1 for a in m.schedule.agents if a.strategy == 'B')
            }
        )
        self.datacollector.collect(self)

    def step(self):
        # Esegue un passo della simulazione (tutti gli agenti eseguono il loro ciclo)
        self.schedule.step()
        self.datacollector.collect(self)  # Salva i dati raccolti

    def game(self, s1, s2):
        # Definizione della matrice dei payoff per il gioco
        matrix = {
            'A': {'A': (1, 1), 'B': (0, 0)},  # Payoff se entrambi scelgono A o entrambi B
            'B': {'A': (0, 0), 'B': (2, 2)}   # Payoff se uno sceglie A e l'altro B
        }
        return matrix[s1][s2]

# ---- FUNZIONE DI PLOT DINAMICO ----
def plot_live_all(model, step, fig, axs, A_vals, B_vals, lineA, lineB, max_steps):
    G = model.G
    color_map = {'A': 'blue', 'B': 'orange'}
    agent_colors = [color_map[agent.strategy] for agent in model.schedule.agents]  # Assegna un colore per ogni strategia

    # Visualizzazione del grafo con layout a molla (in alto a sinistra)
    axs[0, 0].clear()
    model.pos = nx.spring_layout(G, pos=model.pos, seed=42, iterations=50)  # Calcola la posizione dei nodi per il layout
    nx.draw(G, pos=model.pos, ax=axs[0, 0], node_color=agent_colors, with_labels=False, node_size=300)  # Disegna il grafo
    labels = {i: str(i) for i in G.nodes}  # Etichetta i nodi
    nx.draw_networkx_labels(G, pos=model.pos, labels=labels, ax=axs[0, 0], font_size=8, font_color="black")  # Aggiungi le etichette
    axs[0, 0].set_title(f"Spring Layout - Step {step}")  # Titolo del grafico

    # Area plot per la distribuzione delle strategie (in alto a destra)
    axs[0, 1].clear()
    x = range(len(A_vals))  # Asse delle x basato sul numero di passi
    axs[0, 1].fill_between(x, A_vals, color='blue', alpha=0.6, label='Strategy A')  # Strategia A
    axs[0, 1].fill_between(x, A_vals, np.array(A_vals) + np.array(B_vals), color='orange', alpha=0.6, label='Strategy B')  # Strategia B
    axs[0, 1].set_title(f"Strategy Distribution Area Plot - Step {step}")
    axs[0, 1].set_xlabel("Step")
    axs[0, 1].set_ylabel("Number of agents")
    axs[0, 1].legend(loc='upper left')  # Legenda
    axs[0, 1].set_xlim(0, max_steps)  # Limita l'asse x al numero massimo di passi
    axs[0, 1].set_ylim(0, model.num_agents)  # Limita l'asse y al numero totale di agenti
    
    # Scatter plot per la distribuzione spaziale (in basso a sinistra)
    axs[1, 0].clear()
    x = [model.pos[i][0] for i in G.nodes]  # Estrai la posizione x dei nodi
    y = [model.pos[i][1] for i in G.nodes]  # Estrai la posizione y dei nodi
    axs[1, 0].scatter(x, y, c=agent_colors, s=150, edgecolor='black', alpha=0.8)  # Disegna i nodi
    axs[1, 0].set_title(f"Spatial Distribution - Step {step}")
    axs[1, 0].set_xlabel("X Position")
    axs[1, 0].set_ylabel("Y Position")
    axs[1, 0].set_xlim(-1, 1)  # Limita la visualizzazione
    axs[1, 0].set_ylim(-1, 1)  # Limita la visualizzazione

    # Grafico temporale per l'evoluzione delle strategie (in basso a destra)
    axs[1, 1].clear()
    axs[1, 1].plot(range(len(A_vals)), A_vals, label='Strategy A', color='blue')  # Grafico per la strategia A
    axs[1, 1].plot(range(len(B_vals)), B_vals, label='Strategy B', color='orange')  # Grafico per la strategia B
    axs[1, 1].set_title("Evolution of strategies")  # Titolo del grafico
    axs[1, 1].set_xlabel("Step")
    axs[1, 1].set_ylabel("Number of agents")
    axs[1, 1].grid(True)
    axs[1, 1].legend()
    axs[1, 1].set_xlim(0, max_steps)
    axs[1, 1].set_ylim(0, model.num_agents)

    # Aggiorna e mostra
    plt.tight_layout()
    plt.pause(0.3)

# ---- ESECUZIONE PRINCIPALE ----
if __name__ == "__main__":
    max_steps = 100                 # Numero di passi per la simulazione
    model = NXNModel(N=100)        # Inizializza il modello con 100 agenti
    A_vals, B_vals = [], []        # Liste per salvare l'evoluzione delle strategie

    # Impostazioni grafiche
    screen_width = 1440
    screen_height = 900
    figsize = (screen_width * 0.75 / 100, screen_height * 0.75 / 100)

    plt.ion()  # Attiva modalità interattiva
    fig, axs = plt.subplots(2, 2, figsize=figsize)

    # Impostazioni grafico temporale
    axs[1, 1].set_xlim(0, max_steps)
    axs[1, 1].set_ylim(0, model.num_agents)
    axs[1, 1].set_title("Evolution of strategies")
    axs[1, 1].set_xlabel("Step")
    axs[1, 1].set_ylabel("Number of agents")
    axs[1, 1].grid(True)
    axs[1, 1].legend()

    # Loop principale della simulazione
    for step in range(max_steps):
        model.step()  # Esegui un passo della simulazione
        model_data = model.datacollector.get_model_vars_dataframe()  # Raccogli i dati
        A_vals.append(model_data["Count_A"].iloc[-1])  # Aggiungi il conteggio della strategia A
        B_vals.append(model_data["Count_B"].iloc[-1])  # Aggiungi il conteggio della strategia B

        # Aggiorna la visualizzazione
        plot_live_all(model, step, fig, axs, A_vals, B_vals, None, None, max_steps)

    plt.ioff()
    plt.show()

    # Esporta i dati in formato CSV alla fine della simulazione
    model_data = model.datacollector.get_model_vars_dataframe()
    model_data.to_csv("strategies_dynamics.csv", index_label="Step")
