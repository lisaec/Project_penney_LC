from src import data_gen
from src import simulation
from src import visualizations

#generate 1,000,000 decks
deck_loc = data_gen.save_decks(1000000)

#run simulation
results, n_games, all_wins = simulation.simulate_games(deck_path = deck_loc)

#Visualize results
visualizations.make_plot(results, 1000000, filename = 'results.png')