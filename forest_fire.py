import mesa
import numpy as np
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt

class FireAgent(mesa.Agent):
    """An agent representing fire or ember."""
    def __init__(self, model, pos, fire_type="fire"):
        super().__init__(model)
        self.model.grid.place_agent(self, pos)
        self.fire_type = fire_type
        self.color_intensity = 1.0  

    def step(self):
        if self.fire_type == "fire":
            neighbors = self.model.grid.get_neighborhood(self.pos, moore=False, include_center=False)
            for neighbor in neighbors:
                if self.model.grid.is_cell_empty(neighbor):
                    if self.model.patches[neighbor] == "green":
                        new_agent = FireAgent(self.model, neighbor, fire_type="fire")
                        self.model.patches[neighbor] = "burned"
                        self.model.burned_trees += 1
            self.fire_type = "ember"
        elif self.fire_type == "ember":
            self.color_intensity -= 0.3
            if self.color_intensity < 0.1:
                self.model.grid.remove_agent(self)
                self.remove()


class ForestFireModel(mesa.Model):
    def __init__(self, width, height, density, seed=None):
        super().__init__(seed=seed)
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.density = density
        self.initial_trees = 0
        self.burned_trees = 0
        self.patches = {}  

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                if self.random.random() < self.density:
                    self.patches[(x, y)] = "green"
                else:
                    self.patches[(x, y)] = "empty"

        # Ignite the first column
        for y in range(self.grid.height):
            if self.patches[(0, y)] == "green":
                fire_agent = FireAgent(self, (0, y), fire_type="fire")
                self.patches[(0, y)] = "burned"
                self.burned_trees += 1

        self.initial_trees = list(self.patches.values()).count("green") + self.burned_trees

        self.datacollector = DataCollector(
            model_reporters={"Percent Burned": lambda m: (m.burned_trees / m.initial_trees * 100) if m.initial_trees else 0}
        )

        self.datacollector.collect(self)
        self.running = True

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
        if len(self.agents) == 0:
            self.running = False

    def get_patch_grid(self):
        grid = np.zeros((self.grid.width, self.grid.height))
        for (x, y), state in self.patches.items():
            if state == "green":
                grid[x, y] = 1  # Green trees
            elif state == "burned":
                grid[x, y] = 2  # Burned trees Red
        return grid.T  

# Run model and results
if __name__ == "__main__":
    model = ForestFireModel(50, 50, 0.6)
    while model.running:
        model.step()

    # Plot final state 0: empty, 1: green, 2: red
    final_grid = model.get_patch_grid()
    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(["white", "green", "red"]) 

    plt.figure(figsize=(6, 6))
    plt.imshow(final_grid, cmap=custom_cmap, vmin=0, vmax=2)
    plt.title("Final State of Forest")
    plt.axis("off")
    plt.show()

    # Plot percent burned over time
    results = model.datacollector.get_model_vars_dataframe()
    results.plot()
    plt.ylabel("% of Trees Burned")
    plt.xlabel("Step")
    plt.title("Forest Fire Spread")
    plt.grid(True)
    plt.show()
