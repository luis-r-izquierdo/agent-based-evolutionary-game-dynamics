import mesa
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mesa import Model
from mesa.space import MultiGrid

# ——— PARAMETRI DEL MODELLO ———
WIDTH = 80                     # LARGHEZZA DELLA GRIGLIA
HEIGHT = 80                    # ALTEZZA DELLA GRIGLIA
STEPS = 100                    # NUMERO DI PASSI DELLA SIMULAZIONE
INITIAL_C_PERCENT = 0.9        # PERCENTUALE INIZIALE DI AGENTI CON STRATEGIA COOPERANTE
    
PAYOFF_CC = 1.0                # VALORI DEI PAYOFF
PAYOFF_CD = 0.0                
PAYOFF_DC = 1.7                
PAYOFF_DD = 0.0                

payoff_matrix = np.array([          # MATRICE DEI PAYOFF
    [PAYOFF_CC, PAYOFF_CD],
    [PAYOFF_DC, PAYOFF_DD]
])

class CustomRandomActivation:               # CLASSE PER LA GESTIONE DELLA SCHEDULAZIONE
    def __init__(self, model):              # INIZIALIZZAZIONE CON IL METODO INIT 
        self.model = model                  # MODELLO
        self.agents = []                    # LISTA DEGLI AGENTI  

    def add(self, agent):                   # AGGIUNGE UN AGENTE ALLA LISTA
        self.agents.append(agent)           # INSERTA L'AGENTE NELLA LISTA    

    def step(self):                                                     # ESEGUE UN PASSO PER OGNI AGENTE              
        for agent in random.sample(self.agents, k=len(self.agents)):    
            agent.step()                                                
        for agent in self.agents:              
            agent.advance()

    def shuffle_do(self, method_name):                                  # ESEGUE UN METODO PER OGNI AGENTE IN ORDINE CASUALE
        for agent in random.sample(self.agents, k=len(self.agents)):    # ORDINE CASUALE
            getattr(agent, method_name)()    

class ImitateAgent:                                                         # CLASSE PER GLI AGENTI                   
    def __init__(self, unique_id, model):                                   # INIZIALIZZAZIONE CON IL METODO INIT
        self.unique_id = unique_id                                          # IDENTIFICATIVO UNICO
        self.model = model                                                                  
        self.strategy = 0 if random.random() < INITIAL_C_PERCENT else 1     # STRATEGIA INIZIALE (0 = C, 1 = D)
        self.payoff = 0.0                                                   # PAYOFF INIZIALE
        self.pos = None                                                     # POSIZIONE NELLA GRIGLIA               

    def update_payoff(self):                                                # FUNZIONE PER AGGIORNARE IL PAYOFF
        # AGGIORNA IL PAYOFF PER L'AGENTE IN BASE AI VICINI
        neighborhood = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)                 # GRIGLIA MOORE
        self.payoff = sum(self.model.payoff_matrix[self.strategy, other.strategy] for other in neighborhood)    # QUI ANDIAMO A PRENDERE IL PAYOFF DALLA MATRICE DEI PAYOFF

    def update_strategy(self):                                              # FUNZIONE PER AGGIORNARE LA STRATEGIA                       
                                                                            # AGGIORNA LA STRATEGIA DELL'AGENTE SCEGLIENDO IL MIGLIOR VICINO
        neighborhood = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)     # VICINANZA VALUTATA SU GRIGLIA MOORE
        max_payoff = max(agent.payoff for agent in neighborhood)                                    # MASSIMO PAYOFF TRA I VICINI ANDIAMO AD ESTRARLO DAI VICINI
        best = [agent for agent in neighborhood if agent.payoff == max_payoff]                      # AGENTI CON PAYOFF MASSIMO
        self.strategy = random.choice(best).strategy                                                # ASSEGNA CASUALMENTE UNA STRATEGIA TRA I MIGLIORI VICINI CON PAYOFF MASSIMO                             

class ImitateBestModel(Model):                                    # CLASSE PER IL MODELLO CHE ESTENDE LA CLASSE MODEL DI MESA                        
    def __init__(self, width, height):                            # INIZIALIZZAZIONE CON IL METODO INIT
        super().__init__()                                        # RICHIAMIAMO LA SUPER CLASSE MODEL
        self.grid = MultiGrid(width, height, torus=False)         # GRIGLIA MULTIAGENTE NON TOROIDALE
        self.schedule = CustomRandomActivation(self)              # SCHEDULER PERSONALIZZATA
        self.payoff_matrix = payoff_matrix                        # MATRICE DEI PAYOFF 

        uid = 0                                                  # IDENTIFICATIVO UNICO INIZIALE
        for x in range(width):                                   # CON IL FOR X ANDIAMO A ITERARE SULLA LARGHEZZA 
            for y in range(height):                              # CON IL FOR Y ANDIAMO A ITERARE SULL'ALTEZZA
                agent = ImitateAgent(uid, self)                  # CREAZIONE DELL'AGENTE ALL'INTERNO DELLA GRIGLIA
                agent.pos = (x, y)                               # POSIZIONE DELL'AGENTE SU COORDINATE X E Y
                self.grid.place_agent(agent, (x, y))             # POSIZIONA L'AGENTE NELLA GRIGLIA
                self.schedule.add(agent)                         # AGGIUNGE L'AGENTE ALLA SCHEDULER
                uid += 1                                         # INCREMENTIAMO L'IDENTIFICATIVO UNICO

    def step(self):                                             # FUNZIONE PER ESEGUIRE UN PASSO DEL MODELLO              
        self.schedule.shuffle_do("update_payoff")               # RICORRIAMO A SHUFFLE DO PER AGGIORNARE IL PAYOFF DEGLI AGENTI
        self.schedule.shuffle_do("update_strategy")             # RANDOMIZZIAMO L'ORDINE DEGLI AGENTI E AGGIORNIAMO LA STRATEGIA

    def get_grid_array(self):                                       # FUNZIONE PER OTTENERE LA GRIGLIA COME ARRAY 
        arr = np.zeros((WIDTH, HEIGHT))                             # INIZIALIZZA UN ARRAY DI ZERI DELLA DIMENSIONE DELLA GRIGLIA
        for x in range(WIDTH):                                      # ANDIAMO A ITERARE SULLA LARGHEZZA
            for y in range(HEIGHT):                                 # ANDIAMO A ITERARE SULL'ALTEZZA
                cell = self.grid.get_cell_list_contents([(x, y)])   # OTTENIAMO IL CONTENUTO DELLA CELLA
                if cell:                                            # SE LA CELLA NON È VUOTA
                    arr[x, y] = cell[0].strategy                    # ASSEGNA IL VALORE DELLA STRATEGIA ALL'ARRAY
        return arr  

    def count_strategies(self):                                              # FUNZIONE PER CONTEGGIARE LE STRATEGIE               
        num_C = sum(1 for a in self.schedule.agents if a.strategy == 0)      # NUMERO DI AGENTI CON STRATEGIA COOPERANTE
        num_D = sum(1 for a in self.schedule.agents if a.strategy == 1)      # NUMERO DI AGENTI CON STRATEGIA NON COOPERANTE
        total = len(self.schedule.agents)                                    # NUMERO TOTALE DI AGENTI      
        return num_C, num_D, 100 * num_C / total, 100 * num_D / total        # PERCENTUALE DI AGENTI CON STRATEGIA COOPERANTE 
                                                                             # E NON COOPERANTE CON UN SEMPICE CALCOLO MATEMATICO
# ——— ANIMAZIONE E GRAFICO ———
def update(frame):    # FUNZIONE PER AGGIORNARE L'ANIMAZIONE E IL GRAFICO
    model.step()      # AGGIORNAMENTO DEL MODELLO A OGNI PASSO

    # aggiorna griglia
    grid = model.get_grid_array()       # OTTENIAMO LA GRIGLIA COME ARRAY
    im.set_array(grid.T)                # TRASPOSTIAMO LA GRIGLIA PER LA VISUALIZZAZIONE
    ax.set_title(f"Distribuzione delle Strategie – Passo {frame+1}")  # AGGIORNAMENTO DEL TITOLO CON IL PASSO CORRENTE

    # conteggi
    num_C, num_D, perc_C, perc_D = model.count_strategies()         # CONTEGGIO DELLE STRATEGIE
    counter_C.set_text(f"C: {num_C} ({perc_C:.1f}%)")               # AGGIORNAMENTO DEL TESTO DEL COUNTER C
    counter_D.set_text(f"D: {num_D} ({perc_D:.1f}%)")               # AGGIORNAMENTO DEL TESTO DEL COUNTER D

    # aggiorna curve
    x_data.append(frame+1)                         # AGGIUNGE IL PASSO ALLA LISTA X
    y_data_C.append(perc_C)                        # AGGIUNGE LA PERCENTUALE C ALLA LISTA Y               
    y_data_D.append(perc_D)                        # AGGIUNGE LA PERCENTUALE D ALLA LISTA Y
    line_C.set_data(x_data, y_data_C)              # AGGIORNAMENTO DELLA CURVA C
    line_D.set_data(x_data, y_data_D)              # AGGIORNAMENTO DELLA CURVA D

    # STAMPA A TERMINALE OGNI 25 PASSI PARTENDO DA STEP 0 
    if (frame+1) % 25 == 0:                                                             # INIZIA CON CONTROLLO DI PASSI
        print(f"Step {frame+1}: C={num_C} ({perc_C:.1f}%), D={num_D} ({perc_D:.1f}%)")    # AGGIUNGE IL PASSO ALLA STAMPA

    return [im, counter_C, counter_D, line_C, line_D]             # RESTITUISCE LA LISTA DELLE VARIABILI DA AGGIORNARE

if __name__ == "__main__":                                          # INIZIO DEL PROGRAMMA DEFINIZIONE STANDARD
    model = ImitateBestModel(WIDTH, HEIGHT)                         # RICHIAMA DEL MODELLO CON LARGHEZZA E ALTEZZA DEFINITE

    # STAMPA A TERMINALE I CONTEGGI NELLE STRATEGIE 
    num_C, num_D, perc_C, perc_D = model.count_strategies()                     # CONTEGGIO DELLE STRATEGIE
    print(f"Step 0: C={num_C} ({perc_C:.1f}%), D={num_D} ({perc_D:.1f}%)")      # AGGIUNGE IL PASSO ALLA STAMPA

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 6))                       # CREAZIONE DELLA FIGURA E DEI SOTTO-GRAFICI

    # GRAFICO SINISTRO
    im = ax.imshow(model.get_grid_array().T, cmap="coolwarm", origin="lower", animated=True)  # CREAZIONE DELLA GRIGLIA CON IMSHOW
    ax.set_xticks(np.arange(0, WIDTH, 5))                                                     # AGGIUNGE LE GRIGLIE SULL'ASSE X
    ax.set_yticks(np.arange(0, HEIGHT, 5))                                                    # AGGIUNGE LE GRIGLIE SULL'ASSE Y
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("Distribuzione delle Strategie")

    # COUNTER SOTTO IL GRAFICO PER NUMERO E PERCENTUALE DI AGENTI C E D
    counter_C = ax.text(0.3, -0.12, "", transform=ax.transAxes, ha='center', fontsize=11, color='blue')
    counter_D = ax.text(0.7, -0.12, "", transform=ax.transAxes, ha='center', fontsize=11, color='red')

    # GRAFICO DESTRO
    ax2.set_xlim(0, STEPS)               # LIMITE ASSE X PER FARLO AGGIORNARE FINO A STEPS
    ax2.set_ylim(0, 100)                 # LIMITE ASSE Y 
    ax2.set_xlabel("Passi")
    ax2.set_ylabel("Percentuale")
    ax2.set_title("Evoluzione % C e D")
    line_C, = ax2.plot([], [], label="COOP", color='blue', linewidth=2)
    line_D, = ax2.plot([], [], label="DEFEZ", color='red', linewidth=2)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc='upper right')

    # dati per grafico
    x_data, y_data_C, y_data_D = [], [], []

    # ANIMAZIONE PER AGGIORNARE IL GRAFICO CON LE CURVE
    ani = FuncAnimation(fig, update, frames=STEPS, interval=100, blit=False, repeat=False)

    plt.tight_layout()   # MOSTRA IL GRAFICO PIU COMPATTO
    plt.show()        # MOSTRA IL GRAFICO
