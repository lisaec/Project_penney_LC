# Project_penney_LC
 
This is my penny game simulation repository!! It is composed of three main python files


## Quick Start:

To practice creating decks, running the simulation, and saving a visualization, use the **run_simulations.ipynb** notebook

## data_gen.py
This file contains all the data generating functions. It can generate and save decks from a specific random state. 

## main_simulation.py
this file contains the main simulation of the card games. It has a function "play_game" to play the game once on a deck, and it has a function "simulate_games" to simulate and save data for all possible games in a set of decks


## visualizations.py
this file contains one function to generate a file with two heatmaps of the results for tricks and for cards

This project is still very far from perfect. I would like to edit the mechanism by which seeds are saved and reopened, as I'm not entirely sure that it is restoring the state as I would like it to. 

I would also like to add more complex visualizations in the future, but these heatmaps are a preliminary result. 