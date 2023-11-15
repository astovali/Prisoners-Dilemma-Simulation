from bots.always_cooperate import AlwaysCooperateBot
from bots.always_cheat import AlwaysCheatBot
from bots.copycat import CopyCatBot
from bots.grudge import GrudgeBot
from itertools import combinations

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
    'always_cheat': AlwaysCheatBot(),
    'copycat': CopyCatBot(),
    'grudge': GrudgeBot()
}

#runs a game between two bots
def run_game(bot_names, rounds, output=False, reset_hardness=False):
    #load up the bots
    bot_1 = bots[bot_names[0]]
    bot_2 = bots[bot_names[1]]

    bot_1_score_total = 0
    bot_2_score_total = 0

    #run the game
    for i in range(rounds):
        #find the moves of the bots
        bot_1_move = bot_1.move(bot_2)
        bot_2_move = bot_2.move(bot_1)

        #find their scores
        bot_1_score, bot_2_score = results[bot_1_move][bot_2_move]

        bot_1_score_total += bot_1_score
        bot_2_score_total += bot_2_score

        #add these to the results
        bot_1.update([bot_1_move, bot_2_move], bot_1_score)
        bot_2.update([bot_2_move, bot_1_move], bot_2_score)
    
    #give results
    if output:
        print(f'Results for {bot_1.name} vs {bot_2.name}:')
        print(bot_1)
        print(f'This game score: {bot_1_score_total}\n')
        print(bot_2)
        print(f'This game score: {bot_2_score_total}\n')
        if bot_1_score_total > bot_2_score_total:
            print(f'Winner is {bot_1.name}')
        elif bot_1_score_total < bot_2_score_total:
            print(f'Winner is {bot_2.name}')
        else:
            print('Game was a draw')
        print()
    bot_1.reset(reset_hardness)
    bot_2.reset(reset_hardness)

for i, j in combinations(bots.keys(), 2):
    run_game([i, j], 10, output=True)
print('Final results: ')
sorted_bots = sorted(bots.keys(), key=lambda bot: -bots[bot].score)
for i in sorted_bots:
    print(f'{i} with a score of {bots[i].score}')