import mesa
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Matrice dei payoff per il gioco Carta-Forbice-Sasso
# 0 = Carta, 1 = Forbice, 2 = Sasso
payoffs = np.array([[0, -1, 1],
                    [1, 0, -1],
                    [-1, 1, 0]])

class EGD3x3ImitateModel(mesa.Model):
    """Modello con agenti che adottano strategie in stile Carta-Forbice-Sasso."""

    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.running = True
        self.prob_revision = 0.1  # Probabilità di revisione della strategia

        # Crea gli agenti
        agents = EGD3x3ImitateAgent.create_agents(model=self, n=n)

        self.datacollector = mesa.DataCollector(
            agent_reporters={"Current_strategy": "strategy"},
        )

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("update_strategy")

class EGD3x3ImitateAgent(mesa.Agent):
    """Agente con strategia iniziale casuale."""

    def __init__(self, model):
        super().__init__(model)
        self.strategy = self.random.choice([0, 1, 2])  # 0 = Carta, 1 = Forbice, 2 = Sasso

    def update_payoff(self):
        others = [x for x in self.model.agents if x != self]
        if others:
            other = self.random.choice(others)
            self.payoff = payoffs[self.strategy, other.strategy]
            other.payoff = payoffs[other.strategy, self.strategy]

    def update_strategy(self):
        if self.random.random() < self.model.prob_revision:
            others = [x for x in self.model.agents if x != self]
            if others:
                other = self.random.choice(others)
                if other.payoff > self.payoff:
                    self.strategy = other.strategy

# Inizializzazione del modello
model = EGD3x3ImitateModel(n=500, width=10, height=10)

# Numero di passi temporali
steps = 2000

# Collezione dei dati
strategy_data = []

for step in range(steps):
    model.step()
    agent_strategy = [agent.strategy for agent in model.agents]
    strategy_data.append(agent_strategy)

# Conversione in DataFrame
df_strategy = pd.DataFrame(strategy_data)

# Reshape in formato lungo
df_strategy_melted = df_strategy.melt(var_name="Agent", value_name="Strategy", ignore_index=False)
df_strategy_melted['Step'] = np.tile(np.arange(steps), len(model.agents))

# Mappa strategia numerica → etichetta testuale
strategy_labels = {0: "Carta", 1: "Forbice", 2: "Sasso"}
df_strategy_melted["StrategyLabel"] = df_strategy_melted["Strategy"].map(strategy_labels)

# Plot con legenda gestita da seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df_strategy_melted, x='Step', hue='StrategyLabel',
             multiple='stack', palette='Set2', discrete=True)

plt.title("Evoluzione delle Strategie degli Agenti (Carta, Forbice, Sasso)")
plt.xlabel("Passo")
plt.ylabel("Numero di Agenti")
plt.tight_layout()
plt.show()
