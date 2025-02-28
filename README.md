# Project_penney_LC
 
This is my penny game simulation repository!! It is composed of three main python files


## Quick Start:

To practice creating decks, running the simulation, and saving a visualization, use the **run_simulations.ipynb** notebook

## data_gen.py
This file contains all the data generating functions. It can generate and save decks from a specific random state. It also can add decks
to a current deck to add simulations

## main_simulation.py
this file contains the main simulation of the card games. It has a function "play_game" to play the game once on a deck, and it has a function "simulate_games" to simulate and save data for all possible games in a set of decks


## visualizations.py
this file contains one function to generate a file with two heatmaps of the results for tricks and for cards

This project is still very far from perfect. I realized that it is impossible to add new simulations to old simulations the way my simulate
games is currently set up, so i need to rework that. Currently the only way to do this is to add decks to old decks and to restart the simulation. I am probably going to split up the simulate games function into 3 different functions, one to simulate each combination, one to add together the combinations, and one to reshape the output for visualization.

I would like to edit the mechanism by which seeds are saved and reopened, as I'm not entirely sure that it is restoring the state as I would like it to. 

I would also like to add more complex visualizations in the future, but these heatmaps are a preliminary result. 