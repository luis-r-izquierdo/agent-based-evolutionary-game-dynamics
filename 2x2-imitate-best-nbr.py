import mesa
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mesa.datacollection import DataCollector 
from itertools import product

# ——— PARAMETRI DEL MODELLO ———
WIDTH = 80                    # LARGHEZZA DELLA GRIGLIA
HEIGHT = 80                    # ALTEZZA DELLA GRIGLIA
STEPS = 1000                  # NUMERO DI PASSI DELLA SIMULAZIONE
INITIAL_C_PERCENT = 0.9        # PERCENTUALE INIZIALE DI AGENTI CON STRATEGIA COOPERANTE
    
PAYOFF_CC = 1.0                # VALORI DEI PAYOFF
PAYOFF_CD = 0.0                
PAYOFF_DC = 1.7                
PAYOFF_DD = 0.0                

payoff_matrix = np.array([          # MATRICE DEI PAYOFF
    [PAYOFF_CC, PAYOFF_CD],
    [PAYOFF_DC, PAYOFF_DD]
])

class ImitateAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.strategy = 0 if random.random() < INITIAL_C_PERCENT else 1
        self.payoff = 0.0
        self.pos = None


    def update_payoff(self):        #aggiunto
         # Calcola il payoff
        neighborhood = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)
        self.payoff = sum(self.model.payoff_matrix[self.strategy, other.strategy] for other in neighborhood)

    def update_strategy(self):      #aggiunto
        # Aggiorna la strategia basandosi sui payoff attuali
        neighborhood = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)
        max_payoff = max(agent.payoff for agent in neighborhood)
        best = [agent for agent in neighborhood if agent.payoff == max_payoff]
        self.strategy = random.choice(best).strategy
    


class ImitateBestModel(mesa.Model):                     
    def __init__(self, width, height, seed=None):
        super().__init__(seed=seed)
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.payoff_matrix = payoff_matrix 
   
        self.datacollector = DataCollector(
            model_reporters={
                "Percent_C": lambda m: m.count_strategies()[2],
                "Percent_D": lambda m: m.count_strategies()[3]
            },
        )

        #aggiunto
        positions = list(product(range(width), range(height)))  # tutte le coordinate (x, y)
        agents = ImitateAgent.create_agents(model=self, n=width * height)
        
        for agent, pos in zip(agents, positions):

        # il posizionamento manuale degli agenti non è necessario e manda in conflitto le posizioni
        # generando il warning visto nel terminale.
        # rimuovendo la riga seguente, posizioniamo gli agenti automaticamente nella griglia
        #    agent.pos = pos
            self.grid.place_agent(agent, pos)

        self.datacollector.collect(self)

    def step(self):             
        # commentato step perché non necessario in questo modello e soprattutto perché non viene mai definito nell'agent
        # quindi si potrebbe procedere con la rimozione definitiva dal codice.

        # self.agents.shuffle_do("step")
        self.agents.shuffle_do("update_payoff")
        self.agents.shuffle_do("update_strategy")
        self.datacollector.collect(self)

    def get_grid_array(self):
        arr = np.zeros((WIDTH, HEIGHT))
        for x in range(WIDTH):
            for y in range(HEIGHT):
                cell = self.grid.get_cell_list_contents([(x, y)])
                if cell:
                    arr[x, y] = cell[0].strategy
        return arr  

    def count_strategies(self):
        num_C = sum(1 for a in self.agents if a.strategy == 0)
        num_D = sum(1 for a in self.agents if a.strategy == 1)
        total = len(self.agents)
        return num_C, num_D, 100 * num_C / total, 100 * num_D / total  



# ——— ANIMAZIONE E GRAFICO ———
def update(frame):
    model.step()

    grid = model.get_grid_array()
    im.set_array(grid.T)
    ax.set_title(f"Distribuzione delle Strategie – Passo {frame+1}")

    num_C, num_D, perc_C, perc_D = model.count_strategies()
    counter_C.set_text(f"C: {num_C} ({perc_C:.1f}%)")
    counter_D.set_text(f"D: {num_D} ({perc_D:.1f}%)")

    x_data.append(frame + 1)
    y_data_C.append(perc_C)               
    y_data_D.append(perc_D)
    line_C.set_data(x_data, y_data_C)
    line_D.set_data(x_data, y_data_D)

    if (frame + 1) % 25 == 0:
        print(f"Step {frame + 1}: C={num_C} ({perc_C:.1f}%), D={num_D} ({perc_D:.1f}%)")

    return [im, counter_C, counter_D, line_C, line_D]

if __name__ == "__main__":
    model = ImitateBestModel(WIDTH, HEIGHT)

    num_C, num_D, perc_C, perc_D = model.count_strategies()
    print(f"Step 0: C={num_C} ({perc_C:.1f}%), D={num_D} ({perc_D:.1f}%)")

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    im = ax.imshow(model.get_grid_array().T, cmap="coolwarm", origin="lower", animated=True)
    ax.set_xticks(np.arange(0, WIDTH, 5))
    ax.set_yticks(np.arange(0, HEIGHT, 5))
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("Distribuzione delle Strategie")

    counter_C = ax.text(0.3, -0.12, "", transform=ax.transAxes, ha='center', fontsize=11, color='blue')
    counter_D = ax.text(0.7, -0.12, "", transform=ax.transAxes, ha='center', fontsize=11, color='red')

    ax2.set_xlim(0, STEPS)
    ax2.set_ylim(0, 100)
    ax2.set_xlabel("Passi")
    ax2.set_ylabel("Percentuale")
    ax2.set_title("Evoluzione % C e D")
    line_C, = ax2.plot([], [], label="COOP", color='blue', linewidth=2)
    line_D, = ax2.plot([], [], label="DEFEZ", color='red', linewidth=2)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc='upper right')

    x_data, y_data_C, y_data_D = [], [], []

    ani = FuncAnimation(fig, update, frames=STEPS, interval=100, blit=False, repeat=False)

    plt.tight_layout()
    plt.show()

    model_data = model.datacollector.get_model_vars_dataframe()
    print("\nDati raccolti dal DataCollector (prime 5 righe):")
    print(model_data.head())
