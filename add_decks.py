from src import data_gen
from src import simulation
from src import visualizations
import pandas as pd
import os
import json

#read in existing results to add to
old_results = pd.read_csv('data/results_1000000_decks_20250324204019.csv')

with open("data/wins_1000000_decks_20250324204019.json", 'r') as f:
    old_wins = json.load(f)

#create new decks
deck_loc = data_gen.save_decks(10000, seed_path = 'init_state_20250324202029.json')


#run simulation
results, n_games, all_wins = simulation.add_decks(old_wins, old_results, deck_loc, n_old_games = 1000000)

#Visualize results
visualizations.make_plot(results, n_games, filename = 'more_results.png')