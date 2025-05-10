#%%
import mesa

# Data visualization tools.
import seaborn as sns
from matplotlib import pyplot as plt

# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd



class ForestFire(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.running = True
        self.burned_trees = 0

        # Create agents
        agents = MoneyAgent.create_agents(model=self, n=n)
        # Create x and y positions for agents
        x = self.rng.integers(0, self.grid.width, size=(n,))
        y = self.rng.integers(0, self.grid.height, size=(n,))
        for a, i, j in zip(agents, x, y):
            # Add the agent to a random grid cell
            self.grid.place_agent(a, (i, j))

        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": "wealth", "Steps_not_given": "steps_not_given"},
        )

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("move")
        self.agents.shuffle_do("give_money")

def ignite_left_side(self):
    """Ignite all trees on the left side of the grid (x = 0)."""
    for y in range(self.grid.height):  # Iterate over all rows
        cell_contents = self.grid.get_cell_list_contents([(0, y)])  # Get agents in the leftmost column
        for agent in cell_contents:
            agent.ignite()


class ForestAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, model):
        super().__init__(model)
        self.burned = False
        self.color = "green"  # Default color for a tree


    def ignite(self):
        """Ignite the tree, turning it into fire."""
        self.color = "red"  # Fire color
        self.burned = True
        self.model.burned_trees += 1


    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        cellmates.pop(cellmates.index(self))
        if len(cellmates) > 0 and self.wealth > 0:
            other = self.random.choice(cellmates)
            other.wealth += payoffs[other.my_choice][self.my_choice]
            self.wealth += payoffs[self.my_choice][other.my_choice]
            self.steps_not_given = 0
        else:
            self.steps_not_given += 1


model = MoneyModel(100, 10, 10)
for _ in range(20):
    model.step()





tot_wealths = np.zeros((model.grid.width, model.grid.height))
for cell_content, (x, y) in model.grid.coord_iter():
    tot_wealth = sum([x.wealth for x in cell_content])
    tot_wealths[x][y] = tot_wealth
# Plot using seaborn, with a visual size of 5x5
g = sns.heatmap(tot_wealths, cmap="viridis", annot=True, cbar=False, square=True)
g.figure.set_size_inches(5, 5)
g.set(title="total wealth on each cell of the grid");
plt.show()        
# %%
