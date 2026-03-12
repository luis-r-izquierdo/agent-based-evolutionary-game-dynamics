import mesa
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd
import random

payoffs={'H':{'H':-1,'D':2, "R":-1 }, 'D':{'H':0,'D':1, "R": 1}, "R": {"H":-1, "D":1, "R":1}}

class Model(mesa.Model):
     
     def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.running = True
        self.prob_revision = 0.995
        self.grid = mesa.space.MultiGrid(width, height, True)

        #Strategy creation
        self.strategies = ["H"] * (3280) + ["D"] * (3280) + ["R"] * (1)
        self.random.shuffle(self.strategies)

        #Agent creation
        agents = Agent.create_agents(model=self, n=n)
        # Create x and y coordinates for agents
        available_cells = [(x, y) for x in range(self.grid.width) for y in range(self.grid.height)]
        # shuffle cells
        self.rng.shuffle(available_cells)
        
        # matching agents with cells, one agent for one cell
        for a, (i, j) in zip(agents, available_cells):
            self.grid.place_agent(a, (i, j))

        self.datacollector = mesa.DataCollector(
        agent_reporters={"Payoff": "payoff", "Total_Payoff": "tot_payoff", "Current_strategy": "strategy"},
        )
    
     def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("find_strategy")
        self.agents.shuffle_do("update_strategy")

class Agent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.strategy = model.strategies.pop()
         # next strategy
        self.future_strategy = self.strategy
        # one iteration payoff
        self.payoff = 0 
        self.tot_payoff = 0
        
    
    def update_payoff(self):
        # find neighbors
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)
        self.payoff = 0
        # updating payoff
        for neighbor in neighbors:
                self.payoff += payoffs[self.strategy][neighbor.strategy]
        self.tot_payoff += self.payoff


    def find_strategy(self):
        if self.random.random() < self.model.prob_revision:
            neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)
             # finding best neighbor and choosing from the best
            best_neighbor = max(neighbors, key=lambda x: x.payoff, default=None)
            if neighbors:
                max_payoff = max(n.payoff for n in neighbors)
                best_neighbors = [n for n in neighbors if n.payoff == max_payoff]
                chosen = self.random.choice(best_neighbors)
                self.future_strategy = chosen.strategy
        else:
            self.future_strategy = random.choice(["H", "D", "R"])
    
    def update_strategy(self):
        self.strategy = self.future_strategy



model = Model(6561, 81, 81, 26)

for _ in range(1000):
    model.step()

# data collectiong
agent_data = model.datacollector.get_agent_vars_dataframe()

df_reset = agent_data.reset_index()
r_proportions = df_reset[df_reset["Current_strategy"] == "R"].groupby("Step").size() / model.num_agents

# Plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=r_proportions, marker="o", label="% di agenti con strategia 'R'")
plt.title("Evoluzione della strategia 'R' nel tempo")
plt.xlabel("Step")
plt.ylabel("Percentuale di 'R'")
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.show()

# final payoff values
latest_step = agent_data.index.get_level_values("Step").max()
final_payoff = agent_data.xs(latest_step, level="Step")["Payoff"]

final_total_payoff = agent_data.xs(latest_step, level="Step")["Total_Payoff"]

# creating final payoff's histplot
plt.figure(figsize=(8, 5))
sns.histplot(final_total_payoff, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel("Payoff Totale")
plt.ylabel("Numero di agenti")
plt.title("Distribuzione del payoff totale tra gli agenti")
plt.show()

# saving final strategies
final_strategy = agent_data.xs(latest_step, level="Step")["Current_strategy"]

# creating final strategies histplot
plt.figure(figsize=(8, 5))
sns.histplot(final_strategy, bins=3, edgecolor='black', alpha=0.7, stat="percent")
plt.xlabel("Strategia")
plt.ylabel("Numero di agenti")
plt.title("Distribuzione delle strategie")
plt.show()



# possible strategies
strategy_map = {"R": 0, "D": 1, "H": 2}

#grid creation
strategy_grid = np.full((model.grid.height, model.grid.width), np.nan)

for x in range(model.grid.width):
    for y in range(model.grid.height):
        cell_contents = model.grid.get_cell_list_contents([(x, y)])
        if len(cell_contents) > 0:
            agent = cell_contents[0]
            strategy_grid[y, x] = strategy_map[agent.strategy]

# personalized colormap
custom_cmap = ListedColormap(["red", "blue", "yellow"])

# Visualization
plt.figure(figsize=(14, 14))  
g = sns.heatmap(
    strategy_grid,
    cmap=custom_cmap,
    cbar=False,
    square=True,
    linewidths=0.05,
    linecolor='gray',
    xticklabels=False, 
    yticklabels=False
)
g.set(title="Strategia finale per cella della griglia")

# legend
red_patch = mpatches.Patch(color='red', label='R (Retaliator)')
blue_patch = mpatches.Patch(color='blue', label='D (Dove)')
yellow_patch = mpatches.Patch(color='yellow', label='H (Hawk)')
plt.legend(handles=[red_patch, blue_patch, yellow_patch], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()