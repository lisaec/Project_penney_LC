import numpy as np
import pandas as pd
import random
import datetime

import os
import json 
from importlib import reload


HALF_DECK_SIZE = 26

def get_decks(n_decks: int, seed: 'rng', 
              half_deck_size: int = HALF_DECK_SIZE, 
              ) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate `n_decks` shuffled decks using NumPy.
    
    Returns:
        decks (np.ndarray): 2D array of shape (n_decks, num_cards), 
        each row is a shuffled deck.

    """
    init_deck = [0]*half_deck_size + [1]*half_deck_size
    decks = np.tile(init_deck, (n_decks, 1))
    seed.permuted(decks, axis=1, out=decks)

    return decks

def init_seed(filepath = "data"):
    """creates a first seedpath to use when generating decks
        and returns the filename of the seed"""
    
    rng = np.random.default_rng()
    
    new_seed_file = f"state_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    # Save the state
    state = rng.bit_generator.state
    seed_path_out = f"{filepath}/{new_seed_file}"
    
    with open(seed_path_out, 'w') as f:
        json.dump(state, f)
     
    return new_seed_file
    

def save_decks(n_decks: int, seed_path = None, filepath = "data") -> str:
    
    """Saves n decks using a random state saved in seed_path
        If no seedpath is given, it will generate a new random state
        returns name of file storing decks"""
    
    if seed_path == None:
        seed_path = init_seed()
    
    rng = np.random.default_rng()
    
    #opening state from seed_path
    with open(f'{filepath}/{seed_path}', 'r') as f:
        rng.bit_generator.state = json.load(f)
    
    #gen decks
    decks = get_decks(n_decks, rng)
    
    deck_file = f"{filepath}/decks_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.npy"
    
    #save_decks
    np.save(deck_file, decks)
    
    # Save the state
    state = rng.bit_generator.state
    seed_path_out = f"{filepath}/state_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    
    with open(seed_path_out, 'w') as f:
        json.dump(state, f)

    return deck_file