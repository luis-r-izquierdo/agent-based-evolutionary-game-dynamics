#%%
import mesa

# Data visualization tools.
import seaborn as sns
from matplotlib import pyplot as plt

import numpy as np

# Data manipulation and analysis.
import pandas as pd

payoffs={'A':{'A':1,'B':0}, 'B':{'A':0,'B':2}}



class EGD2x2ImitateModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.running = True
        self.prob_revision = 0.1

        # Create agents
        agents = EGD2x2ImitateAgent.create_agents(model=self, n=n)

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
        others = [x for x in self.model.agents if x != self]
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
