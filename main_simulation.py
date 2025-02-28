import numpy as np
import pandas as pd

#defining all possible sequences
SEQUENCES = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [1, 0, 0],
    [0, 1, 1],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]


#making a list of combinations of the sequences
COMBINATIONS = [(player_1_seq, player_2_seq) for player_1_seq in SEQUENCES for player_2_seq in SEQUENCES]



def play_game(deck: 'arr', player_1_seq: list, player_2_seq: list) -> dict:
    
    "Scores a game, returning scores, tricks, and winners in a dictionary"
    
    if player_1_seq == player_2_seq:
        output =  {'player_1_seq': str(player_1_seq),
                'player_2_seq': str(player_2_seq),
                'player_1_score': None, 
                'player_2_score': None, 
                'player_1_tricks': None,
                'player_2_tricks': None,
                'winner_cards': None,
                'winner_tricks':None}
            
        return output
    
    #converting array to list
    deck = list(map(int, deck))
    
    #setting up scores
    player_1_score, player_2_score = 0,0
    player_1_tricks, player_2_tricks = 0,0
    
    #setting up base for while loop
    #idk why the way i converted the array to a list its using 1 as the lowest index?
    top_card = 3
    batch = 0
    
    #while cards left in deck, keep playing
    while top_card <= len(deck):

        #what are the three most recent flipped cards
        current_seq = list(deck[top_card-3:top_card])
        
        #are those player 1s cards?
        if current_seq == player_1_seq:
            #add score, batch is # of flipped cards not in most recent 3
            player_1_score += (3 + batch)
            player_1_tricks += 1
            
            #reset batch
            batch = 0
            #flip 3 cards
            top_card += 3

        if current_seq == player_2_seq:
            player_2_score += (3 + batch)
            player_2_tricks += 1

            batch = 0
            top_card += 3

        else:
            #batch gets bigger
            batch += 1
            #flip over another card
            top_card += 1
            
        
        #scoring games
        if player_1_score > player_2_score:
            winner_cards = "player_1"
            
        elif player_1_score == player_2_score:
            winner_cards = "tie"
            
        else:
            winner_cards = "player_2"
            
        if player_1_tricks > player_2_tricks:
            winner_tricks = "player_1"
            
            
        elif player_1_tricks == player_2_tricks:
            winner_tricks = "tie"
            
        else:
            winner_tricks = "player_2"
            
    
            
    output =   {'player_1_seq': str(player_1_seq),
                'player_2_seq': str(player_2_seq),
                'player_1_score':player_1_score, 
                'player_2_score':player_2_score, 
                'player_1_tricks':player_1_tricks,
                'player_2_tricks':player_2_tricks,
                'winner_cards': winner_cards,
                'winner_tricks':winner_tricks}
        
    return output
        
    

def simulate_games(deck_path: 'filepath', combinations = COMBINATIONS) -> "arrays":
    
    """ Simulates games played on all submitted decks on all combinations given in combinations 
    
    returns a record of all combination outcomes, and arrays of percentage likelihood of card wins, trick wins,
    card ties and trick ties for each combination
    """
    decks = np.load(deck_path)
    
    #creating an empty dataframe of results
    results = pd.DataFrame(columns = ('player_1_seq',
                                    'player_2_seq',
                                    'player_1_wins_cards', 
                                    'ties_cards', 
                                    'player_1_wins_tricks',
                                    'ties_tricks'))

    #simulate games for each combination
    for (player_1_seq, player_2_seq) in combinations:
    
        #creating a dictionary recording wins 
        wins_dict = {
        'player_1_seq':str(player_1_seq),
        'player_2_seq':str(player_2_seq),
        'player_1_wins_cards':0,
        'ties_cards':0,
        'player_1_wins_tricks':0,
        'ties_tricks':0
        }

        #if players are the same sequence, make results null
        if player_1_seq == player_2_seq:
            wins_dict = {
            'player_1_seq':str(player_1_seq),
            'player_2_seq':str(player_2_seq),
            'player_1_wins_cards':None,
            'ties_cards':None,
            'player_1_wins_tricks':None,
            'ties_tricks':None
            }

        #play the game on each deck and save when player 1 wins
        for deck in decks:
            game_dict = play_game(deck, player_1_seq = player_1_seq, player_2_seq = player_2_seq)

            if game_dict['winner_cards'] == 'player_1':
                wins_dict['player_1_wins_cards'] += 1

            elif game_dict['winner_cards'] == 'tie':
                wins_dict['ties_cards'] += 1  

            if game_dict['winner_tricks'] == 'player_1':
                wins_dict['player_1_wins_tricks'] += 1

            elif game_dict['winner_tricks'] == 'tie':
                wins_dict['ties_tricks'] += 1 

        #convert that to a DF
        wins_dict_df = pd.DataFrame(wins_dict, index = [0])
        
        #add that to the total results
        results = pd.concat([results, wins_dict_df])
        
    #reshape card results to be an array
    results_cards = results[['player_1_seq', 'player_2_seq', 'player_1_wins_cards']]

    results_cards_matrix = pd.pivot_table(results_cards, values = 'player_1_wins_cards', index = 'player_1_seq', 
                                     columns = 'player_2_seq').astype(float)
    
    ties_cards = results[['player_1_seq', 'player_2_seq', 'ties_cards']]

    ties_cards_matrix = pd.pivot_table(ties_cards, values = 'ties_cards', index = 'player_1_seq', 
                                     columns = 'player_2_seq').astype(float)
       
    #reshape card results to be an array
    results_tricks = results[['player_1_seq', 'player_2_seq', 'player_1_wins_tricks']]

    results_tricks_matrix = pd.pivot_table(results_tricks, values = 'player_1_wins_tricks', index = 'player_1_seq', 
                                     columns = 'player_2_seq').astype(float)
    
    ties_tricks = results[['player_1_seq', 'player_2_seq', 'ties_tricks']]

    ties_tricks_matrix = pd.pivot_table(ties_tricks, values = 'ties_tricks', index = 'player_1_seq', 
                                     columns = 'player_2_seq').astype(float)
    
    #calculate win rate pct instead of total
    results_cards_rate = results_cards_matrix/len(decks)* 100
    results_tricks_rate = results_tricks_matrix/len(decks)* 100
    ties_cards_rate = ties_cards_matrix/len(decks) * 100
    ties_tricks_rate = ties_tricks_matrix/len(decks) * 100
    
   

    return results, results_cards_rate, results_tricks_rate, ties_cards_rate, ties_tricks_rate

