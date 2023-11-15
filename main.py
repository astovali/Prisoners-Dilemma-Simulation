from bots.always_cooperate import AlwaysCooperateBot
from bots.always_cheat import AlwaysCheatBot

#Table of results
results = {
    True: {True: (2, 2),
        False: (-1, 3)},
    False: {True: (3, -1),
        False: (0, 0)}
}

#Remember to add your bot into the bot dictionary
bots = {
    'always_cooperate': AlwaysCooperateBot(),
    'always_cheat': AlwaysCheatBot()
}

#runs a game between two bots
def run_game(bot_names, rounds):
    #load up the bots
    bot_1 = bots[bot_names[0]]
    bot_2 = bots[bot_names[1]]

    #place them into a separate list
    game_dict = [bot_1, bot_2]

    #run the game
    for i in range(rounds):
        #find the moves of the bots
        bot_1_move = bot_1.move(game_dict)
        bot_2_move = bot_2.move(game_dict)

        #find their scores
        bot_1_score, bot_2_score = results[bot_1_move][bot_2_move]

        #add these to the results
        bot_1.update(bot_1_move, bot_1_score)
        bot_2.update(bot_2_move, bot_2_score)
    
    #give results
    print('Results:')
    print(bot_1)
    print(bot_2)

run_game(['always_cooperate', 'always_cheat'], 10)
