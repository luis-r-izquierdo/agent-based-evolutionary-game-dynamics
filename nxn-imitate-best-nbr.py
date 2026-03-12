###################################Codice generale######################################
############best_nbr_model################
import mesa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Matrice di payoff casuale
payoffs = np.array([
    [-1,  2,  0],  
    [ 0,  1,  1],  
    [ 1,  1,  1]   
])

N_STRATEGIES = 3
STRATEGY_LABELS = {0: "Hawk", 1: "Dove", 2: "Retaliator"}


class NxNImitateBestNeighborModel(mesa.Model):
    """Modello con agenti che imitano i vicini."""

    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.running = True
        self.width = width
        self.height = height
        self.prob_revision = 0.1  # Probabilità di revisione della strategia

        # Crea gli agenti
        agents = NxNImitateBestNeighborAgent.create_agents(model=self, n=n)

        self.datacollector = mesa.DataCollector(
            agent_reporters={"Current_strategy": "strategy"},
        )

    def step(self):
        self.compute_neighbors()
        self.datacollector.collect(self)
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("update_strategy")

    def compute_neighbors(self):
        for agent in self.agents:
            agent.neighbors = [
                other for other in self.agents
                if agent != other and self.is_neighbor(agent.pos, other.pos)
            ]

    def is_neighbor(self, pos1, pos2):
        dx = abs(pos1[0] - pos2[0])
        dy = abs(pos1[1] - pos2[1])
        dx = min(dx, self.width - dx)
        dy = min(dy, self.height - dy)
        return dx <= 1 and dy <= 1
        
class NxNImitateBestNeighborAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.strategy = self.random.randrange(N_STRATEGIES)
        self.payoff = 0
        self.pos = (self.random.randrange(model.width), self.random.randrange(model.height))

    def update_payoff(self):
        neighbors = [a for a in self.model.custom_agents if self.is_neighbor(a)]
        self.payoff = sum(payoffs[self.strategy, other.strategy] for other in neighbors)

    def update_strategy(self):
        neighbors = [a for a in self.model.custom_agents if self.is_neighbor(a)]
        if not neighbors:
            return
        best = max(neighbors, key=lambda a: a.payoff)
        if best.payoff > self.payoff and self.random.random() < self.model.prob_revision:
            self.strategy = best.strategy


# Inizializzazione e simulazione
model = NxNImitateBestNeighborModel(n=100, width=10, height=10)
steps = 200
for step in range(200):
    model.step()

# Estrazione dei dati
df_strategy = model.datacollector.get_agent_vars_dataframe().reset_index()
df_strategy = df_strategy.rename(columns={"Current_strategy": "Strategy"})
df_strategy["StrategyLabel"] = df_strategy["Strategy"].map(STRATEGY_LABELS)

# Aggregazione per passo
df_counts = df_strategy.groupby(["Step", "StrategyLabel"]).size().unstack(fill_value=0)

# Aggiunta del grafico
# Grafico ad area per mostrare la composizione nel tempo
plt.figure(figsize=(12, 7))

# Calcolo delle proporzioni
df_props = df_counts.div(df_counts.sum(axis=1), axis=0)

# Disegna grafico ad area
plt.stackplot(
    df_props.index,
    [df_props[strategy] for strategy in df_props.columns],
    labels=df_props.columns,
    colors=plt.cm.tab10.colors[:len(df_props.columns)],
    alpha=0.8
)

plt.title("Composizione Strategica nel Tempo", fontsize=16)
plt.xlabel("Passo di Simulazione", fontsize=14)
plt.ylabel("Proporzione di Agenti", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title="Strategie", loc="upper right", fontsize=12, title_fontsize=13)
plt.tight_layout()
plt.show()

#######################################ESERCIZIO 1######################################
#Modello di Hawk-Dove-Retaliator-Bully
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mesa
import matplotlib.animation as animation

# Matrice Hawk-Dove-Retaliator-Bully
payoffs = np.array([
    [-1, 2, -1, 2],  # Hawk
    [ 0, 1, 1, 0],   # Dove
    [-1, 1, 1, 2],   # Retaliator
    [ 0, 2, 0, 1]    # Bully
])

N_STRATEGIES = 4
STRATEGY_LABELS = {0: "Hawk", 1: "Dove", 2: "Retaliator", 3: "Bully"}

# Inizializzazione
model = NxNImitateBestNeighborModel(n=100, width=10, height=10) 

# Simulazione
steps = 200
for _ in range(steps):
    model.step()

# Estrazione dei dati
df_strategy = model.datacollector.get_agent_vars_dataframe().reset_index() # Raccoglie i dati degli agenti
df_strategy = df_strategy.rename(columns={"Current_strategy": "Strategy"}) 
df_strategy["StrategyLabel"] = df_strategy["Strategy"].map(STRATEGY_LABELS)

# Aggregazione per passo temporale
df_counts = df_strategy.groupby(["Step", "StrategyLabel"]).size().unstack(fill_value=0)

#Set up del grafico

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Aggregazione dei dati
df_counts = df_strategy.groupby(["Step", "StrategyLabel"]).size().unstack(fill_value=0)
df_counts = df_counts.reset_index()

# Colori leggibili e distintivi
color_map = {
    'Hawk': '#e41a1c',
    'Dove': '#377eb8',
    'Retaliator': '#4daf4a',
    'Bully': '#ff7f00'
}
strategy_labels = df_counts.columns[1:]  # esclude 'Step'

# Setup figura
fig, ax = plt.subplots(figsize=(12, 6))

# Funzione di aggiornamento per l'animazione
def update(frame):
    ax.clear()
    ax.set_xlim(0, df_counts['Step'].max())
    ax.set_ylim(0, df_counts[strategy_labels].values.sum(axis=1).max() * 1.1)
    ax.set_title("Evoluzione Strategie - Grafico ad Area", fontsize=14)
    ax.set_xlabel("Passo", fontsize=12)
    ax.set_ylabel("Numero di Agenti", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)

    current_data = df_counts.iloc[:frame + 1]
    ys = [current_data[label] for label in strategy_labels]

    ax.stackplot(current_data['Step'], ys, 
                 labels=strategy_labels, 
                 colors=[color_map[label] for label in strategy_labels],
                 alpha=0.85)
    ax.legend(title="Strategia", loc='upper left')

ani = animation.FuncAnimation(fig, update, frames=len(df_counts), interval=100)

plt.tight_layout()
plt.show()

# Per salvare
# ani.save("Esercizio_1.gif", writer='pillow', fps=10)

#######################################ESERCIZIO 2######################################
##########CONDIZIONI BILANCIATE#########
import mesa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Definizione della matrice dei payoffs monociclica con 5 strategie
payoffs = np.array([
    [ 0, -1,  0,  0,  1], 
    [ 1,  0, -1,  0,  0],
    [ 0,  1,  0, -1,  0],
    [ 0,  0,  1,  0, -1],
    [-1,  0,  0,  1,  0]
])

N_STRATEGIES = 5
STRATEGY_LABELS = {i: f"Strategy_{i}" for i in range(N_STRATEGIES)} 

# Definizione della classe dell'agente
class NxNImitateBestNeighborAgent(mesa.Agent):
    def __init__(self, model, strategy=None): 
        super().__init__(model)
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = self.random.randrange(N_STRATEGIES) # Strategia iniziale casuale
        self.payoff = 0 # Inizializza payoff a 0
        self.pos = (self.random.randrange(model.width), self.random.randrange(model.height)) # Posizione casuale nella griglia

    def update_payoff(self):
        # Calcola il payoff sommando i risultati dei confronti con i vicini
        neighbors = [a for a in self.model.custom_agents if self.is_neighbor(a)]
        self.payoff = sum(payoffs[self.strategy, other.strategy] for other in neighbors)

    def update_strategy(self):
        # Aggiorna la strategia imitando il vicino col payoff migliore
        neighbors = [a for a in self.model.custom_agents if self.is_neighbor(a)] 
        if not neighbors: # Se non ci sono vicini, non fa nulla
            return
        best = max(neighbors, key=lambda a: a.payoff) # Trova il vicino col payoff migliore
        # Se il vicino ha un payoff migliore, aggiorna la strategia con probabilità prob_revision
        if best.payoff > self.payoff and self.random.random() < self.model.prob_revision:
            self.strategy = best.strategy

    def is_neighbor(self, other): # Determina se un altro agente è vicino (considerando bordo toroidale)
        dx = abs(self.pos[0] - other.pos[0])
        dy = abs(self.pos[1] - other.pos[1])
        dx = min(dx, self.model.width - dx)
        dy = min(dy, self.model.height - dy)
        return dx <= 1 and dy <= 1 and other != self
    
# Definizione del modello
class NxNImitateBestNeighborModel(mesa.Model):
    def __init__(self, n, width, height, balanced=True, seed=None): 
        super().__init__(seed=seed)
        self.num_agents = n # Numero di agenti
        self.width = width # Larghezza della griglia
        self.height = height # Altezza della griglia
        self.running = True # Stato del modello
        self.prob_revision = 0.9
        self.custom_agents = []

        # Inizializzazione bilanciata o sbilanciata
        if balanced:
            per_strategy = n // N_STRATEGIES
            remaining = n % N_STRATEGIES
            all_strategies = [i for i in range(N_STRATEGIES) for _ in range(per_strategy)]
            all_strategies += [self.random.randrange(N_STRATEGIES) for _ in range(remaining)]
            self.random.shuffle(all_strategies)
        else:
            all_strategies = [0] * n  # Tutti iniziano con la strategia 0

# Crea agenti con le strategie definite
        for s in all_strategies:
            agents = NxNImitateBestNeighborAgent(self, strategy=s)
            self.custom_agents.append(agents)

        self.datacollector = mesa.DataCollector(
            agent_reporters={"Current_strategy": "strategy"}
        )

    def shuffle_do(self, method_name):
        self.random.shuffle(self.custom_agents)
        for agent in self.custom_agents:
            getattr(agent, method_name)()

    def step(self):
        # Passo di simulazione: raccoglie dati, aggiorna payoff e strategie
        self.datacollector.collect(self)
        self.shuffle_do("update_payoff")
        self.shuffle_do("update_strategy")

# SIMULAZIONE 
model = NxNImitateBestNeighborModel(n=100, width=10, height=10, balanced=True) #Balance=True -> Bilanciato

for _ in range(200):
    model.step()

# Estrazione dei dati
df_strategy = model.datacollector.get_agent_vars_dataframe().reset_index()
df_strategy = df_strategy.rename(columns={"Current_strategy": "Strategy"})
df_strategy["StrategyLabel"] = df_strategy["Strategy"].map(STRATEGY_LABELS)

# Aggregazione per passo
df_counts = df_strategy.groupby(["Step", "StrategyLabel"]).size().unstack(fill_value=0)

# Aggiunta del grafico
plt.figure(figsize=(12, 7))
colors = plt.cm.tab10.colors

for i, strategy in enumerate(df_counts.columns):
    plt.plot(
        df_counts.index,
        df_counts[strategy],
        label=strategy,
        linewidth=2.5,
        color=colors[i % len(colors)]
    )

plt.title("Evoluzione delle Strategie nel Tempo", fontsize=16)
plt.xlabel("Passo di Simulazione", fontsize=14)
plt.ylabel("Numero di Agenti", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title="Strategie", fontsize=12, title_fontsize=13)
plt.tight_layout()
plt.show()

# Animazione
# Mappa strategie a interi per rappresentazione su griglia
width = model.width
height = model.height
steps = len(df_strategy["Step"].unique())

# Ricostruzione della griglia ad ogni step
grids = []
for step in range(steps):
    step_data = df_strategy[df_strategy["Step"] == step]
    grid = np.zeros((height, width), dtype=int)
    for i, agent in enumerate(model.custom_agents):
        x, y = agent.pos
        strategy = step_data.loc[step_data["AgentID"] == i, "Strategy"].values
        if strategy.size > 0:
            grid[y, x] = strategy[0]
    grids.append(grid)

# Creazione animazione
fig, ax = plt.subplots(figsize=(6, 6))
cmap = plt.cm.get_cmap('tab10', N_STRATEGIES)
im = ax.imshow(grids[0], cmap=cmap, vmin=0, vmax=N_STRATEGIES - 1)

def update(frame):
    im.set_data(grids[frame])
    ax.set_title(f"Step {frame}")
    return [im]

ani = animation.FuncAnimation(fig, update, frames=len(grids), interval=200, blit=True)
plt.show()

####CONDIZIONI SBILANCIATE####
import mesa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Matrice monociclica a 5 strategie
payoffs = np.array([
    [ 0, -1,  0,  0,  1],
    [ 1,  0, -1,  0,  0],
    [ 0,  1,  0, -1,  0],
    [ 0,  0,  1,  0, -1],
    [-1,  0,  0,  1,  0]
])

N_STRATEGIES = 5
STRATEGY_LABELS = {i: f"Strategy_{i}" for i in range(N_STRATEGIES)}

class NxNImitateBestNeighborAgent(mesa.Agent):
    def __init__(self, model, strategy=None):
        super().__init__(model)
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = self.random.randrange(N_STRATEGIES)
        self.payoff = 0
        self.pos = (self.random.randrange(model.width), self.random.randrange(model.height))

    def update_payoff(self):
        neighbors = [a for a in self.model.custom_agents if self.is_neighbor(a)]
        self.payoff = sum(payoffs[self.strategy, other.strategy] for other in neighbors)

    def update_strategy(self):
        neighbors = [a for a in self.model.custom_agents if self.is_neighbor(a)]
        if not neighbors:
            return
        best = max(neighbors, key=lambda a: a.payoff)
        if best.payoff > self.payoff and self.random.random() < self.model.prob_revision:
            self.strategy = best.strategy
        # probabilità di mutazione (1%) -> probabilità che un agente cambi strategia casualmente, anche se nessuno ha un payoff migliore
        if self.random.random() < 0.01:
            self.strategy = self.random.randrange(N_STRATEGIES)
            return


    def is_neighbor(self, other):
        dx = abs(self.pos[0] - other.pos[0])
        dy = abs(self.pos[1] - other.pos[1])
        dx = min(dx, self.model.width - dx)
        dy = min(dy, self.model.height - dy)
        return dx <= 1 and dy <= 1 and other != self

class NxNImitateBestNeighborModel(mesa.Model):
    def __init__(self, n, width, height, balanced=True, seed=None): 
        super().__init__(seed=seed)
        self.num_agents = n
        self.width = width
        self.height = height
        self.running = True
        self.prob_revision = 0.9
        self.custom_agents = []

        # Inizializzazione bilanciata o sbilanciata
        if balanced:
            per_strategy = n // N_STRATEGIES
            remaining = n % N_STRATEGIES
            all_strategies = [i for i in range(N_STRATEGIES) for _ in range(per_strategy)]
            all_strategies += [self.random.randrange(N_STRATEGIES) for _ in range(remaining)]
            self.random.shuffle(all_strategies)
        else:
            all_strategies = [0] * n  # Tutti iniziano con la strategia 0

        for s in all_strategies:
            agents = NxNImitateBestNeighborAgent(self, strategy=s)
            self.custom_agents.append(agents)

        self.datacollector = mesa.DataCollector(
            agent_reporters={"Current_strategy": "strategy"}
        )

    def shuffle_do(self, method_name):
        self.random.shuffle(self.custom_agents)
        for agent in self.custom_agents:
            getattr(agent, method_name)()

    def step(self):
        self.datacollector.collect(self)
        self.shuffle_do("update_payoff")
        self.shuffle_do("update_strategy")

# SIMULAZIONE 
model = NxNImitateBestNeighborModel(n=100, width=10, height=10, balanced=False) #False -> Sbilanciato

for _ in range(200): 
    model.step()

# Estrazione dei dati
df_strategy = model.datacollector.get_agent_vars_dataframe().reset_index()
df_strategy = df_strategy.rename(columns={"Current_strategy": "Strategy"})
df_strategy["StrategyLabel"] = df_strategy["Strategy"].map(STRATEGY_LABELS)

# Aggregazione per passo
df_counts = df_strategy.groupby(["Step", "StrategyLabel"]).size().unstack(fill_value=0)

# Aggiunta del grafico
plt.figure(figsize=(12, 7))
colors = plt.cm.tab10.colors

for i, strategy in enumerate(df_counts.columns):
    plt.plot(
        df_counts.index,
        df_counts[strategy],
        label=strategy,
        linewidth=2.5,
        color=colors[i % len(colors)]
    )

plt.title("Evoluzione delle Strategie nel Tempo", fontsize=16)
plt.xlabel("Passo di Simulazione", fontsize=14)
plt.ylabel("Numero di Agenti", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title="Strategie", fontsize=12, title_fontsize=13)
plt.tight_layout()
plt.show()

# Animazione
# Mappa strategie a interi per rappresentazione su griglia
width = model.width
height = model.height
steps = len(df_strategy["Step"].unique())

# Ricostruzione della griglia ad ogni step
grids = []
for step in range(steps):
    step_data = df_strategy[df_strategy["Step"] == step]
    grid = np.zeros((height, width), dtype=int)
    for i, agent in enumerate(model.custom_agents):
        x, y = agent.pos
        strategy = step_data.loc[step_data["AgentID"] == i, "Strategy"].values
        if strategy.size > 0:
            grid[y, x] = strategy[0]
    grids.append(grid)

# Creazione animazione
fig, ax = plt.subplots(figsize=(6, 6))
cmap = plt.cm.get_cmap('tab10', N_STRATEGIES)
im = ax.imshow(grids[0], cmap=cmap, vmin=0, vmax=N_STRATEGIES - 1)

def update(frame):
    im.set_data(grids[frame])
    ax.set_title(f"Step {frame}")
    return [im]

ani = animation.FuncAnimation(fig, update, frames=len(grids), interval=200, blit=True)
plt.show()

# Salva l'animazione
ani.save("Sbilanciato.gif", writer='imagemagick', fps=5)

#########################################ESERCIZIO 3######################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mesa
import matplotlib.animation as animation

# Matrice dei guadagni con parametri β ed e
def create_payoff_matrix(beta, e):
    return np.array([
        [1 - beta, 2, 1 - beta + e],  # Hawk vs Hawk, Dove, Retaliator
        [0, 1, 1 - e],                # Dove vs Hawk, Dove, Retaliator
        [1 - beta - e, 1 + e, 1],     # Retaliator vs Hawk, Dove, Retaliator
    ])

N_STRATEGIES = 3
STRATEGY_LABELS = {0: "Hawk", 1: "Dove", 2: "Retaliator"}

class NxNImitateBestNeighborModel(mesa.Model):
    def __init__(self, n, width, height, beta, e, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.width = width
        self.height = height
        self.running = True
        self.prob_revision = 0.1
        self.payoffs = create_payoff_matrix(beta, e)
        agents = NxNImitateBestNeighborAgent.create_agents(model=self, n=n)

        self.datacollector = mesa.DataCollector(
            agent_reporters={"Current_strategy": "strategy"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("update_strategy")

class NxNImitateBestNeighborAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.strategy = self.random.randrange(N_STRATEGIES)
        self.payoff = 0
        self.pos = (self.random.randrange(model.width), self.random.randrange(model.height))

    def update_payoff(self):
        neighbors = [a for a in self.model.agents if self.is_neighbor(a)]
        self.payoff = sum(self.model.payoffs[self.strategy, other.strategy] for other in neighbors)

    def update_strategy(self):
        neighbors = [a for a in self.model.agents if self.is_neighbor(a)]
        if not neighbors:
            return
        best = max(neighbors, key=lambda a: a.payoff)
        if best.payoff > self.payoff and self.random.random() < self.model.prob_revision:
            self.strategy = best.strategy

    def is_neighbor(self, other):
        dx = abs(self.pos[0] - other.pos[0])
        dy = abs(self.pos[1] - other.pos[1])
        dx = min(dx, self.model.width - dx)
        dy = min(dy, self.model.height - dy)
        return dx <= 1 and dy <= 1 and other != self

# Nuova simulazione su intervallo di beta
beta_values = np.linspace(0.4, 3.6, 200)
final_proportions = []

for beta in beta_values:
    model = NxNImitateBestNeighborModel(n=4900, width=70, height=70, beta=beta, e=0)
    for _ in range(150):
        model.step()

    proportions = []
    for _ in range(10):
        model.step()
        df = model.datacollector.get_agent_vars_dataframe().reset_index()
        latest = df[df["Step"] == df["Step"].max()]
        counts = latest["Current_strategy"].value_counts(normalize=True)
        h = counts.get(0, 0)
        d = counts.get(1, 0)
        r = counts.get(2, 0)
        proportions.append([h, d, r])

    mean_props = np.mean(proportions, axis=0)
    final_proportions.append([beta] + mean_props.tolist())

# Conversione in DataFrame per grafico
df_final = pd.DataFrame(final_proportions, columns=["Beta", "Hawk", "Dove", "Retaliator"])

# Grafico simile a Figura 4
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_final["Beta"], df_final["Hawk"], "s", label="Hawk")
ax.plot(df_final["Beta"], df_final["Dove"], "+", label="Dove")
ax.plot(df_final["Beta"], df_final["Retaliator"], "x", label="Retaliator")

ax.set_xlabel(r"$\\beta$")
ax.set_ylabel("proportion of different strategies")
ax.set_title("Proporzioni finali delle strategie vs $\\beta$")
ax.set_ylim(0, 1.05)
ax.legend()
plt.tight_layout()
plt.show()



