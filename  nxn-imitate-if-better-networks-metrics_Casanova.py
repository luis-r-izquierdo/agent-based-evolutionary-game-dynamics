import mesa
import matplotlib.animation as animation
from matplotlib.cm import ScalarMappable
from mesa import Agent, Model
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
import numpy as np
import random
import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

payoffs = {'A': {'A': 1, 'B': 0}, 'B': {'A': 0, 'B': 2}}

class GameModel(Model):
    """A model with a fixed number of players and selectable network type."""

    def __init__(self, N, width, height, graph_type="erdos", seed=None):
        super().__init__(seed=seed)
        self.num_agents = N
        self.running = True
        self.prob_revision = 0.1
        self.graph_type = graph_type

        # Choose network type
        if graph_type == "erdos":
            self.G = nx.erdos_renyi_graph(n=N, p=0.1, seed=seed)
        elif graph_type == "watts":
            self.G = nx.watts_strogatz_graph(n=N, k=10, p=0.1, seed=seed)
        elif graph_type == "barabasi":
            self.G = nx.barabasi_albert_graph(n=N, m=5, seed=seed)
        else:
            raise ValueError("Invalid graph_type. Use 'erdos', 'watts', or 'barabasi'.")

        self.apply_noise(noise_prob=0.03)

        self.net = NetworkGrid(self.G)

        for i, node in enumerate(self.G.nodes()):
            strategy = "A" if i < 70 else "B"
            a = Player(i, self, strategy)
            self.net.place_agent(a, node)

        self.datacollector = DataCollector(
            agent_reporters={"Wealth": "wealth", "Current_strategy": "strategy"},
        )

    def apply_noise(self, noise_prob=0.03):
        edges_to_consider = list(self.G.edges())
        for u, v in edges_to_consider:
            if self.random.random() < noise_prob:
                self.G.remove_edge(u, v)
                new_u = self.random.randrange(self.num_agents)
                new_v = self.random.randrange(self.num_agents)
                while new_u == new_v or self.G.has_edge(new_u, new_v):
                    new_u = self.random.randrange(self.num_agents)
                    new_v = self.random.randrange(self.num_agents)
                self.G.add_edge(new_u, new_v)

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("update_strategy")


class Player(Agent):
    def __init__(self, unique_id, model, strategy):
        super().__init__(model)
        self.strategy = strategy
        self.payoff = 0
        self.wealth = 1
        self.name = unique_id

    def update_payoff(self):
        neighbors_nodes = self.model.net.get_neighborhood(self.pos, include_center=False)
        others = self.model.net.get_cell_list_contents(neighbors_nodes)
        if len(others) > 0:
            other = self.random.choice(others)
            other.wealth += payoffs[other.strategy][self.strategy]
            self.wealth += payoffs[self.strategy][other.strategy]

    def update_strategy(self):
        if self.random.random() < self.model.prob_revision:
            neighbors_nodes = self.model.net.get_neighborhood(self.pos, include_center=False)
            others = self.model.net.get_cell_list_contents(neighbors_nodes)
            if len(others) > 0:
                other = self.random.choice(others)
                if other.wealth > self.wealth:
                    self.strategy = other.strategy


# --- Batch Runner ---
num_runs = 300
num_steps = 5000
network_type = "watts"  # Change this to "erdos", "watts", or "barabasi"

final_results = []

for run in range(num_runs):
    print(f"\n--- Run {run + 1} of {num_runs} ---")

    model = GameModel(N=100, width=10, height=10, graph_type=network_type, seed=run)

    for step in range(num_steps):
        model.step()

    data = model.datacollector.get_agent_vars_dataframe()
    last_step = data.index.get_level_values(0).max()
    final_data = data.xs(last_step, level="Step")
    count_A = (final_data["Current_strategy"] == "A").sum()
    count_B = (final_data["Current_strategy"] == "B").sum()
    final_results.append({"run": run, "A": count_A, "B": count_B})

df_results = pd.DataFrame(final_results)
df_results.to_csv("final_strategy_counts.csv", index=False)

plt.figure(figsize=(8, 5))
sns.histplot(df_results['A'], kde=False, bins=20, color='skyblue')
plt.title(f"Distribution of Strategy A After {num_steps} Steps ({network_type.title()} Network)")
plt.xlabel("Number of Agents Using Strategy A")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

