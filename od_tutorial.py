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


class ODModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, N, mu=0.1, tolerance=0.2):
        super().__init__()
        self.num_agents = N
        self.mu = mu  # Convergence parameter
        self.tolerance = tolerance  # Tolerance parameter (d)
        self.running = True


        # Create agents
        for i in range(self.num_agents):
            a = ODAgent(self)

        self.datacollector = mesa.DataCollector(
                        agent_reporters={"opinion": "opinion"},
        )            

    def step(self):
        """Advance the model by one step."""
        self.agents.shuffle_do("exchange_opinion")
        self.datacollector.collect(self)

        

class ODAgent(mesa.Agent):
    """An agent with an opinion."""

    def __init__(self, model):
        # Pass the parameters to the parent class.
        super().__init__(model)

        # Create the agent's variable and set the initial values.
        self.opinion = model.random.random()

    def exchange_opinion(self):
        """Update the agent's opinion based on interaction with another agent."""
        other_agent = self.random.choice(self.model.agents)
        # Check if the absolute difference in opinions is within tolerance
        if abs(self.opinion - other_agent.opinion) <= self.model.tolerance:
            # Update opinions based on the Deffuant model
            delta_opinion = self.model.mu * (self.opinion - other_agent.opinion)
            other_agent.opinion += delta_opinion
            self.opinion -= delta_opinion


if __name__ == '__main__':

    #%%
    # Run the model
    model = ODModel(N=2000, mu=0.5, tolerance=0.2)  # Set tolerance (d) to 0.2
    num_steps = 50
    for _ in range(num_steps):
        model.step()


    #%%
    # Collect and visualize final data out of data collector
    opinion_history = model.datacollector.get_agent_vars_dataframe()

    # Reset the index to make it easier to work with
    opinion_history = opinion_history.reset_index()

    # Plot opinions over time
    plt.figure(figsize=(10, 6))
    for agent_id in opinion_history["AgentID"].unique():
        agent_data = opinion_history[opinion_history["AgentID"] == agent_id]
        plt.plot(agent_data["Step"], agent_data["opinion"], linewidth=0.5, alpha=0.7)

    plt.title("Opinion Dynamics Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Opinion")
    plt.show()
    # %%
