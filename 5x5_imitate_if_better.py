import mesa
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# new payoff 5x5 rock-paper-scissors-lizard-spock
payoffs = np.array([[0, 1, 1, -1, -1], 
                    [-1, 0, -1, 1, 1], 
                    [-1, 1, 0, 1, -1],
                    [1, -1, -1, 0, 1],
                    [1, -1, 1, -1, 0]] 
                     )

class EGD5x5ImitateModel(mesa.Model):
    """A model with some number of agents and 5 strategies (like rock-paper-scissors-lizard-spock)."""
    
    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.running = True
        self.prob_revision = 0.1     # change self.prob_revision to modify the outcome
        
        # Create agents
        agents = EGD5x5ImitateAgent.create_agents(model=self, n=n)
        
        self.datacollector = mesa.DataCollector(
            agent_reporters={"Current_strategy": "strategy"},
        )

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("update_strategy")


class EGD5x5ImitateAgent(mesa.Agent):
    """An agent with fixed initial strategy."""
    
    def __init__(self, model):
        super().__init__(model)
        self.strategy = self.random.choice([0, 1, 2, 3, 4])  # 5 possible strategies (rock, paper, scissors, lizard, spock)

    def update_payoff(self):
        others = [x for x in self.model.agents if x != self]
        if len(others) > 0:
            other = self.random.choice(others)
            # Use the payoff matrix to update the interaction between strategies
            self.payoff = payoffs[self.strategy, other.strategy]
            other.payoff = payoffs[other.strategy, self.strategy]

    def update_strategy(self):
        if self.random.random() < self.model.prob_revision:  # Revision chance
            others = [x for x in self.model.agents if x != self]
            if len(others) > 0:
                other = self.random.choice(others)
                if other.payoff > self.payoff:  # Imitation rule: imitating better outcomes
                    self.strategy = other.strategy


# Model initialization (1st argoument num of agents) (still in a grid 10x10, dunno if right) (opt. 4th argoument = fixed seed)
model = EGD5x5ImitateModel(100, 10, 10)

# Number of steps
steps = 1000

# List to collect strategy data
strategy_data = []

# Run the model and collect strategy data at each step
for step in range(steps):
    model.step()
    # Collect strategies for each agent
    agent_strategy = [agent.strategy for agent in model.agents]
    # Create a DataFrame where each row corresponds to a step and each column to an agent's strategy
    strategy_data.append(agent_strategy)

# Convert strategy data to a DataFrame for easy plotting
df_strategy = pd.DataFrame(strategy_data)  

# Melt the DataFrame to create a long format
df_strategy_melted = df_strategy.melt(var_name="Agent", value_name="Strategy", ignore_index=False)
df_strategy_melted['Step'] = np.tile(np.arange(steps), len(model.agents))

# Plot the evolution of strategies over time
plt.figure(figsize=(10, 6))
sns.histplot(data=df_strategy_melted, x='Step', hue='Strategy', multiple='stack', palette='Set2', discrete=True)
plt.title("Evoluzione delle Strategie degli Agenti (Tipo Carta, Forbice, Sasso, Lizard, Spock) - Istogramma Stacked")
plt.xlabel("Passo")
plt.ylabel("Numero di Agenti")
plt.legend(title="Strategia", labels=["Carta", "Forbice", "Sasso","Lizard", "Spock"])
plt.show()
