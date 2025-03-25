# Project Penney

 The Penney card game is a simple 2 player card game played on a single deck. To play the game, each player chooses a sequence of 3 card colors, and the dealer begins to flip over cards. If a players sequence comes up in the deck, then that player wins the trick and all of the flipped over cards. While this game may appear completely random, if players are not blindly choosing their sequences, the second player to select their sequence can choose strategically and almost guarantee a win. The trick is simply to interrupt the opposing players win by choosing the inverse of their second color, their first color, then their second color. For instance, if player 1 chooses RBR, then player 2 should strategically choose RRB to maximize their chance of winning.
 In this repository, I have created code to simulate hundreds of thousands of shuffled decks and play every possible combination of sequence selections. I then process the results and create heatmaps to show the likelihood of winning each game by number of cards and number of tricks.

## Simulation Results
After simulating every combination of sequences on 1 million decks, here were the preliminary results.

![image](https://github.com/user-attachments/assets/ad383da4-1e0c-4c7f-80dd-dafc2e6bb27b)

These results were created in **Main.py**

## Quick Start:
This repository has the capability to generate and save decks, run simulations, add additional simulations to existing game outcomes, and visualize the results.

For a step-by-step example workflow of creating decks, running the simulation, adding additional decks and saving visualizations, check out the **run_simulations.ipynb** notebook.

### I am grading this project and just want to add decks:
For an example of adding decks to existing results, you can use **add_decks.py**

## Source code:
#### data_gen.py
This file contains all the data generating functions. It can generate and save decks from a specific random state. 

#### simulation.py
This file contains the main simulation of the card games. It has a function "play_game" to play the game once on a deck, it has a function "simulate_combination" to simulate many iterations of one combination of player choices, it has a function "simulate_games" to simulate and save data for all possible games in a set of decks, and it has a function "process_results" used to create more usable arrays out of the results. It also has the function "add_decks" to add additional iterations of games to existing results.

#### visualizations.py
this file contains one function to generate a file with two heatmaps of the results for tricks and for cards.
