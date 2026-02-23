import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from mesa import Agent, Model
from mesa.datacollection import DataCollector


class Player(Agent):


   def __init__(self, unique_id, strategy, model):
       self.unique_id = unique_id
       self.model = model
       self.strategy = strategy
       self.strategy_after_revision = strategy
       self.payoff = 0


   def update_payoff(self):
       self.payoff = self.model.payoff_to_use(self)


   def update_strategy_after_revision(self):
       if random.random() < self.model.prob_revision:
           if random.random() < self.model.noise:
               self.strategy_after_revision = random.randint(0, self.model.n_of_strategies - 1)
           else:
               others = [p for p in self.model.players if p.unique_id != self.unique_id]
               if others:
                   observed_player = self.model.random.choice(others)
                   if observed_player.payoff > self.payoff:
                       self.strategy_after_revision = observed_player.strategy


   def update_strategy(self):
       self.strategy = self.strategy_after_revision


class GameModel(Model):


   def __init__(self, n_of_players, payoff_matrix, initial_distribution, noise, payoff_method, prob_revision):
       super().__init__()
       self.num_agents = n_of_players
       self.payoff_matrix = payoff_matrix
       self.n_of_strategies = len(payoff_matrix)
       self.players = []
       self.prob_revision = prob_revision
       self.noise = noise
       self.payoff_method = payoff_method
       self.current_id = 0
       


       self.setup_players(initial_distribution)
       self.data_collector = DataCollector(
           agent_reporters={"strategy": "strategy", "payoff": "payoff"}
       )
       self.strategy_history = []
       self.total_strategy_changes = 0
       self.equilibrium_reached_step = None
       self.last_strategy_snapshot = [p.strategy for p in self.players]



   def next_id(self):
       self.current_id += 1
       return self.current_id - 1


   def setup_players(self, initial_distribution):
       if len(initial_distribution) != self.n_of_strategies:
           raise ValueError("La lunghezza della distribuzione iniziale deve corrispondere al numero di strategie.")


       for i, count in enumerate(initial_distribution):
           for _ in range(count):
               player = Player(self.next_id(), i, self)
               self.players.append(player)


   def payoff_to_use(self, player):
       if self.payoff_method == "expected":
           return self.expected_payoff(player.strategy)
       elif self.payoff_method == "random":
           return self.realized_payoff(player)
       else:
           raise ValueError(f"Metodo di guadagno non valido: {self.payoff_method}")


   def expected_payoff(self, strategy):
       counts = [sum(1 for p in self.players if p.strategy == s) for s in range(self.n_of_strategies)]
       total = sum(counts)
       if total == 0:
           return 0
       probs = [c / total for c in counts]
       return sum(self.payoff_matrix[strategy][s] * p for s, p in enumerate(probs))


   def realized_payoff(self, player):
       others = [p for p in self.players if p.unique_id != player.unique_id]
       if not others:
           return 0
       other = self.random.choice(others)
       return self.payoff_matrix[player.strategy][other.strategy]


   def step(self):
       for player in self.players:
           player.update_payoff()


       for player in self.players:
           player.update_strategy_after_revision()


       strategy_changes = 0
       for idx, player in enumerate(self.players):
            if player.strategy_after_revision != player.strategy:
                strategy_changes += 1
            player.update_strategy()
       self.total_strategy_changes += strategy_changes


       self.update_strategy_expected_payoffs()


       self.data_collector.collect(self)


       strategy_counts = [0] * self.n_of_strategies
       for player in self.players:
           strategy_counts[player.strategy] += 1


       strategy_frequencies = [count / self.num_agents for count in strategy_counts]
       self.strategy_history.append(strategy_frequencies)
       
       current_snapshot = [p.strategy for p in self.players]
       if self.equilibrium_reached_step is None and current_snapshot == self.last_strategy_snapshot:
            self.equilibrium_reached_step = len(self.strategy_history)
       self.last_strategy_snapshot = current_snapshot


   def update_strategy_expected_payoffs(self):
       self.strategy_frequencies = [0] * self.n_of_strategies
       for player in self.players:
           self.strategy_frequencies[player.strategy] += 1
       self.strategy_frequencies = [f / self.num_agents for f in self.strategy_frequencies]


       self.strategy_expected_payoffs = [
           sum(self.payoff_matrix[strategy][s] * self.strategy_frequencies[s] for s in range(self.n_of_strategies))
           for strategy in range(self.n_of_strategies)
       ]


#Analisi Statistiche e Grafiche
def calculate_statistics_df(model, strategy_names):
   strategies = [player.strategy for player in model.players]
   payoffs = [player.payoff for player in model.players]


   stats = {
       'Strategia': [],
       'Media Payoff': [],
       'Varianza Payoff': [],
       'Numero di Giocatori': [],
       'Frequenza': [],
       'Payoff Massimo': [],
       'Payoff Minimo': []
   }


   for strategy in range(model.n_of_strategies):
       strategy_payoffs = [payoffs[i] for i in range(len(payoffs)) if strategies[i] == strategy]
       if strategy_payoffs:
           stats['Strategia'].append(strategy_names[strategy])
           stats['Media Payoff'].append(round(np.mean(strategy_payoffs), 3))  
           stats['Varianza Payoff'].append(round(np.var(strategy_payoffs), 3))  
           stats['Numero di Giocatori'].append(len(strategy_payoffs))
           stats['Frequenza'].append(round(len(strategy_payoffs) / model.num_agents, 3))  
           stats['Payoff Massimo'].append(round(np.max(strategy_payoffs), 3)) 
           stats['Payoff Minimo'].append(round(np.min(strategy_payoffs), 3)) 
       else:
           stats['Strategia'].append(strategy_names[strategy])
           stats['Media Payoff'].append(0)
           stats['Varianza Payoff'].append(0)
           stats['Numero di Giocatori'].append(0)
           stats['Frequenza'].append(0)
           stats['Payoff Massimo'].append(0)
           stats['Payoff Minimo'].append(0)


   stats_df = pd.DataFrame(stats)
   stats_df.loc[len(stats_df.index)] = [  
    '--- Totali / Medi ---',
    '', '', '', '', '', ''
   ]
   avg_changes_per_step = model.total_strategy_changes / len(model.strategy_history)
   time_to_equilibrium = model.equilibrium_reached_step if model.equilibrium_reached_step is not None else "Mai raggiunto"

   stats_df.loc[len(stats_df.index)] = [
    'Cambi strategia / step', avg_changes_per_step, '', '', '', '', ''
   ]
   stats_df.loc[len(stats_df.index)] = [
    'Tempo medio a equilibrio', time_to_equilibrium, '', '', '', '', ''
   ]
   return stats_df


def display_statistics_tables_side_by_side(stats_random, stats_expected):
   stats_random = stats_random.round(3)
   stats_expected = stats_expected.round(3)

   fig, axs = plt.subplots(2, 1, figsize=(20, len(stats_random) + 10)) 
  
   fig.suptitle("Statistiche Finali: Metodo Random vs Expected", fontsize=16, fontweight='bold', y=0.98)
  
   axs[0].axis('off')
   axs[1].axis('off')
   axs[0].set_title("Metodo Random", fontsize=14, fontweight='bold', pad=15)
   axs[1].set_title("Metodo Expected", fontsize=14, fontweight='bold', pad=15)
  
   table0 = axs[0].table(cellText=stats_random.values,
                         colLabels=stats_random.columns,
                         cellLoc='center',
                         loc='center')
   table1 = axs[1].table(cellText=stats_expected.values,
                         colLabels=stats_expected.columns,
                         cellLoc='center',
                         loc='center')
   table0.auto_set_font_size(False)
   table0.set_fontsize(12)
   table0.scale(1.2, 1.8)
  
   table1.auto_set_font_size(False)
   table1.set_fontsize(12)
   table1.scale(1.2, 1.8)
  
   plt.tight_layout(rect=[0, 0.03, 1, 0.95])
   plt.show()


def run_simulation(payoff_method, n_of_players, payoff_matrix, initial_distribution, noise, prob_revision, steps):
   model = GameModel(
       n_of_players=n_of_players,
       payoff_matrix=payoff_matrix,
       initial_distribution=initial_distribution,
       noise=noise,
       payoff_method=payoff_method,
       prob_revision=prob_revision
   )


   for _ in range(steps):
       model.step()
   return model


def run_interactive_simulation(payoff_method, n_of_players, payoff_matrix, initial_distribution, noise, prob_revision, steps):
    print(f"\n🧪 Simulazione Interattiva con metodo: {payoff_method}\n")

    model = GameModel(
        n_of_players=n_of_players,
        payoff_matrix=payoff_matrix,
        initial_distribution=initial_distribution,
        noise=noise,
        payoff_method=payoff_method,
        prob_revision=prob_revision
    )

    strategy_history = []

    fig, axs = plt.subplots(figsize=(10, 6))
    fig.suptitle(f"Evoluzione delle strategie nel tempo - Metodo di Guadagno: {payoff_method}", fontsize=14, fontweight='bold')

    lines = []
    colors = ["skyblue", "salmon", "lightgreen"]
    x_data = []
    y_data = [[] for _ in range(model.n_of_strategies)]

    strategy_labels = {0: "Sasso", 1: "Carta", 2: "Forbice"}

    def init():
        axs.clear()
        axs.set_xlim(0, steps)
        axs.set_ylim(0, 1)
        axs.set_xlabel("Passi")
        axs.set_ylabel("Frequenza")
        axs.set_title("Distribuzione di frequenza delle strategie")
        axs.grid(True)

        for i in range(model.n_of_strategies):
            line, = axs.plot([], [], label=f"Strategia {strategy_labels.get(i, str(i))}", color=colors[i])
            lines.append(line)
        axs.legend(loc='upper right')

        return lines

    def update(frame):
        model.step()
        current_freqs = model.strategy_history[-1]
        strategy_history.append(current_freqs)

        x_data.append(frame)
        for i in range(model.n_of_strategies):
            y_data[i].append(current_freqs[i])
            lines[i].set_data(x_data, y_data[i])

        axs.set_xlim(0, steps)
        return lines

    anim = FuncAnimation(fig, update, frames=steps, init_func=init, blit=False, interval=100, repeat=False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()  # Bloccante


def run_compare_random_expected(n_of_players, payoff_matrix, initial_distribution, noise, prob_revision, steps):
    model_random = GameModel(n_of_players, payoff_matrix, initial_distribution, noise, "random", prob_revision)
    model_expected = GameModel(n_of_players, payoff_matrix, initial_distribution, noise, "expected", prob_revision)

    strategy_history_random = []
    strategy_history_expected = []

    fig, axs = plt.subplots(figsize=(10, 6))  
    fig.suptitle("Confronto Evoluzione Strategie\nMetodo Random vs Expected", fontsize=16, fontweight='bold')

    colors = ["skyblue", "salmon", "lightgreen"]
    strategy_labels = {0: "Sasso", 1: "Carta", 2: "Forbice"}

    x_data = []
    y_data_random = [[] for _ in range(len(payoff_matrix))]
    y_data_expected = [[] for _ in range(len(payoff_matrix))]

    lines_random = []
    lines_expected = []

    def init():
        axs.clear()  
        axs.set_xlim(0, steps)
        axs.set_ylim(0, 1)
        axs.set_title("Frequenza Strategie nel Tempo")
        axs.set_xlabel("Passi")
        axs.set_ylabel("Frequenza")
        axs.grid(True)

        for i in range(len(payoff_matrix)):
            lrand, = axs.plot([], [], label=f"Rand Strat {strategy_labels.get(i,str(i))}", color=colors[i], linestyle='solid')
            lexp, = axs.plot([], [], label=f"Exp Strat {strategy_labels.get(i,str(i))}", color=colors[i], linestyle='dashed')
            lines_random.append(lrand)
            lines_expected.append(lexp)

        axs.legend(loc='upper right')

        return lines_random + lines_expected

    def update(frame):
        model_random.step()
        model_expected.step()

        freqs_random = model_random.strategy_history[-1]
        freqs_expected = model_expected.strategy_history[-1]
        strategy_history_random.append(freqs_random)
        strategy_history_expected.append(freqs_expected)

        x_data.append(frame)
        for i in range(len(payoff_matrix)):
            y_data_random[i].append(freqs_random[i])
            y_data_expected[i].append(freqs_expected[i])
            lines_random[i].set_data(x_data, y_data_random[i])
            lines_expected[i].set_data(x_data, y_data_expected[i])

        axs.set_xlim(0, steps)

        return lines_random + lines_expected

    anim = FuncAnimation(fig, update, frames=steps, init_func=init, blit=False, interval=100, repeat=False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()  # Bloccante

    stats_random = calculate_statistics_df(model_random, list(strategy_labels.values()))
    stats_expected = calculate_statistics_df(model_expected, list(strategy_labels.values()))

    display_statistics_tables_side_by_side(stats_random, stats_expected)
    

if __name__ == "__main__":
   payoff_matrix = np.array([[0, -1, 1],
                             [1, 0, -1],
                             [-1, 1, 0]])
   n_of_players = 500
   initial_distribution = [167, 167, 166]
   noise = 0.05
   prob_revision = 0.95
   steps = 500


   # Simulazioni senza animazione per dati e statistiche 
   model_random = run_simulation("random", n_of_players, payoff_matrix, initial_distribution, noise, prob_revision, steps)
   model_expected = run_simulation("expected", n_of_players, payoff_matrix, initial_distribution, noise, prob_revision, steps)


   # Visualizzazioni e animazioni
   run_interactive_simulation("random", n_of_players, payoff_matrix, initial_distribution, noise, prob_revision, steps)
   run_interactive_simulation("expected", n_of_players, payoff_matrix, initial_distribution, noise, prob_revision, steps)
   run_compare_random_expected(n_of_players, payoff_matrix, initial_distribution, noise, prob_revision, steps)
