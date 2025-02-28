import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def make_plot(filename = str,
              cards = 'DataFrame',
              tricks = 'DataFrame',
              ties_cards = 'DataFrame',
              ties_tricks = 'DataFrame') -> None:

    """makes two heatmaps of game outcomes, one for cards and one for tricks.
        ties are shown in parentheses below win rate
        saves plot as filename given in a folder, heatmaps"""

    # set colortheme
    sns.set_theme(style='white')

    #create subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    #creating label dataframes
    annot_cards = cards.map(lambda x: f"{x:.1f}%") + "\n(" + ties_cards.map(lambda x: f"{x:.1f}%") + ")"
    annot_tricks = tricks.map(lambda x: f"{x:.1f}%") + "\n(" + ties_tricks.map(lambda x: f"{x:.1f}%") + ")"

    #colors
    cmap = sns.color_palette("crest", as_cmap=True).copy()
    cmap.set_bad(color="lightgray")

    # Cards
    sns.heatmap(cards,linewidth=.5, cmap= cmap, ax=axes[0], cbar=False, annot = annot_cards, fmt = "")
    axes[0].set_title("Cards")
    axes[0].set_xlabel("Player 1 Selection")
    axes[0].set_ylabel("Player 2 Selection") 
    axes[0].tick_params(axis='y', rotation=0)

    # Tricks
    sns.heatmap(tricks,linewidth=.5, cmap= cmap, ax=axes[1], cbar=False, annot = annot_tricks, fmt = "")
    axes[1].set_title("Tricks")
    axes[1].set_xlabel("Player 1 Selection")
    axes[1].set_ylabel("Player 2 Selection") 
    axes[1].tick_params(axis='y', rotation=0)

    #whitespace
    plt.subplots_adjust(wspace=0.2)

    #save
    plt.savefig(f'heatmaps/{filename}')
    
    return None