from bots.always_cooperate import AlwaysCooperateBot
from bots.always_cheat import AlwaysCheatBot
from bots.copycat import CopyCatBot
from bots.grudge import GrudgeBot
from bots.copykitten import CopyKittenBot
from bots.fool import FoolBot
from bots.random import RandomBot
from bots.connor import ConnorBot
from itertools import combinations
from random import random

#Table of results
results = {
    True: {True: (2, 2),
        False: (-1, 3)},
    False: {True: (3, -1),
        False: (0, 0)}
}

#Remember to add your bot into the bot dictionary
bots = [
    AlwaysCooperateBot(),
    CopyCatBot(),
    AlwaysCheatBot(),
    GrudgeBot(),
    CopyKittenBot(),
    ConnorBot(),
    AlwaysCooperateBot(),
    CopyCatBot(),
    AlwaysCheatBot(),
    GrudgeBot(),
    CopyKittenBot(),
    ConnorBot(),
    FoolBot(),
    FoolBot()
]

#runs a game between two bots
def run_game(bot_1, bot_2, rounds, output=False, reset_hardness=False, mistake_chance=0.0):
    bot_1_score_total = 0
    bot_2_score_total = 0

    #run the game
    for i in range(rounds):
        #find the moves of the bots
        try:
            bot_1_move = not bot_1.move() if random() < mistake_chance else bot_1.move()
        except Exception as e:
            print(f'{bot_1.name} failed with exception {e}')
            bot_1_move = True
        try:
            bot_2_move = not bot_2.move() if random() < mistake_chance else bot_2.move()
        except Exception as e:
            print(f'{bot_2.name} failed with exception {e}')
            bot_2_move = True

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

matchups = list(combinations(bots, 2))
games = 100
for i in range(games):
    mistake_chance = (i/games) * 0.2
    for a, b in matchups:
        run_game(a, b, 100, output=False, mistake_chance=mistake_chance)

print('Final results: ')
sorted_bots = sorted(bots, key=lambda bot: -bot.score)
said = []
for i in sorted_bots:
    if i.name not in said:
        print(f'{i.name} with a score of {i.score}')
        said.append(i.name)