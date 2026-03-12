#%%
import mesa

# Data visualization tools.
import seaborn as sns
from matplotlib import pyplot as plt
import networkx as nx

import numpy as np

# Data manipulation and analysis.
import pandas as pd

payoffs={'A':{'A':1,'B':0}, 'B':{'A':0,'B':2}}
the_net = [ [1,7], [1,8], [4,7], [7,3], [7,9], [9,5], [5,99], [5,7], [5,8], [99,10], [10,1], [2,7], [9, 2], [2,8], [2,4], [4,7], [4,9], [3,7], 
[99,8], [4,8], [8,10], [8,9]]


class EGD2x2ImitateModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.running = True
        self.prob_revision = 0.1

        self.G = nx.Graph(the_net)
        self.net = mesa.space.NetworkGrid(self.G)


        # Create agents
        for node in self.G.nodes():
            a = EGD2x2ImitateAgent(
                self,
            )

            # Add the agent to the node
            self.net.place_agent(a, node)

        self.datacollector = mesa.DataCollector(
            #model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": "wealth", "Current_strategy": "strategy"},
        )

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("update_strategy")


class EGD2x2ImitateAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1
        self.steps_not_given = 0
        self.strategy = self.random.choice(["A", "B"])


    def update_payoff(self):
        neighbors_nodes = self.model.net.get_neighborhood(
            self.pos, include_center=False
        )
        others=self.model.net.get_cell_list_contents(neighbors_nodes)
        #print(self.model.net.get_cell_list_contents(neighbors_nodes))
        if len(others) > 0 :
            other = self.random.choice(others)
            other.wealth += payoffs[other.strategy][self.strategy]
            self.wealth += payoffs[self.strategy][other.strategy]

    def update_strategy(self):
        if self.random.random() < self.model.prob_revision:  # Fire with probability prob_revision
            others = [x for x in self.model.agents if x != self]
            if len(others) > 0:
                other = self.random.choice(others)
                if other.wealth > self.wealth:
                    self.strategy = other.strategy


model = EGD2x2ImitateModel(100, 10, 10, 42)
for _ in range(20):
    model.step()




# %%