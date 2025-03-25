import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src import simulation

SEQUENCE_NAMES = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB']

def make_plot(results: pd.DataFrame,
              n_games: int,
              filename: str = "results.png") -> None:

    """makes two heatmaps of game outcomes, one for cards and one for tricks.
        ties are shown in parentheses below win rate
        saves plot as filename given in a folder, heatmaps"""

    #process results
    cards, tricks, ties_cards, ties_tricks = simulation.process_results(results, n_games)

    # set colortheme
    sns.set_theme(style='white')

    #create subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    #full title
    plt.suptitle(f"Penney's Game Simulation ({n_games:,} iterations)", fontsize=14, fontweight="bold", y = 0.95)

    #creating label dataframes
    annot_cards = cards.map(lambda x: f"{x:.1f}%") + "\n(" + ties_cards.map(lambda x: f"{x:.1f}%") + ")"
    annot_tricks = tricks.map(lambda x: f"{x:.1f}%") + "\n(" + ties_tricks.map(lambda x: f"{x:.1f}%") + ")"

    #colors
    cmap = sns.color_palette("crest", as_cmap=True).copy()
    cmap.set_bad(color="lightgray")

    # Cards
    sns.heatmap(cards,linewidth=.5, cmap= cmap, ax=axes[0], cbar=False, annot = annot_cards, fmt = "")
    axes[0].set_title("Player 2 wins (Cards)")
    axes[0].set_xlabel("Player 2 Selection")
    axes[0].set_ylabel("Player 1 Selection") 
    axes[0].tick_params(axis='y', rotation=0)
    axes[0].set_xticklabels(SEQUENCE_NAMES)
    axes[0].set_yticklabels(SEQUENCE_NAMES)

    # Tricks
    sns.heatmap(tricks,linewidth=.5, cmap= cmap, ax=axes[1], cbar=False, annot = annot_tricks, fmt = "")
    axes[1].set_title("Player 2 wins (Tricks)")
    axes[1].set_xlabel("Player 1 Selection")
    axes[1].set_ylabel("Player 2 Selection") 
    axes[1].tick_params(axis='y', rotation=0)
    axes[1].set_xticklabels(SEQUENCE_NAMES)
    axes[1].set_yticklabels(SEQUENCE_NAMES)

    #whitespace
    plt.subplots_adjust(wspace=0.2)

    #save
    plt.savefig(f'heatmaps/{filename}')
    
    return None