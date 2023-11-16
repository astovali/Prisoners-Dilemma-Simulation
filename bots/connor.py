from bots.bot_class import Bot
    
class ConnorBot(Bot):
    forgive_thresholds = [0.0001, 0.038]
    grudge_threshold = 0.143

    def __init__(self):
        Bot.__init__(self, 'connor')
        self.reached_last_round = True
        self.mistakes_this_round = 0
        self.randomness = 0
        self.randomness_this_round = 0
        self.intended_move = True
        self.game_length = 0
        self.first_game = True
        self.angry = False

    def reset(self, hard=False):
        Bot.reset(self, hard=hard)
        if not self.reached_last_round:
            self.game_length = int(self.game_length*0.9)
            self.reached_last_round = True
        self.randomness = (self.randomness*5 + self.randomness_this_round)/6
        self.angry = False
        self.mistakes_this_round = 0
        self.randomness_this_round = 0
        if hard:
            self.reached_last_round = True
            self.randomness = 0
            self.game_length = 0
            self.rounds_played = 0
            self.first_game = True

    def store(self, choice):
        self.intended_move = choice
        return choice

    def move(self):
        if self.game_length != 0 and len(self.raw_moves) == 0:
            self.first_game = False
        self.game_length = max(len(self.raw_moves), self.game_length)
        if not self.first_game:
            if self.game_length == len(self.raw_moves):
                self.reached_last_round = True
                return False
        if len(self.raw_moves) >= 1:
            if self.intended_move != self.raw_moves[-1][0]:
                self.mistakes_this_round += 1
        self.randomness_this_round = 0 if len(self.raw_moves) == 0 else self.mistakes_this_round/len(self.raw_moves)
        randomness = (self.randomness*9 + self.randomness_this_round)/10
        if randomness >= self.forgive_thresholds[0] and randomness <= self.forgive_thresholds[1]:
            #play as copykitten
            if len(self.raw_moves) >= 2:
                return self.store(self.raw_moves[len(self.raw_moves)-1][1] or self.raw_moves[len(self.raw_moves)-2][1])
        elif randomness >= self.grudge_threshold:
            #play as always grudge
            if self.angry:
                return self.store(False)
            if len(self.raw_moves) >= 1:
                if self.raw_moves[len(self.raw_moves)-1][1] == False:
                    self.angry = True
                    return self.store(False)
        else:
            #play as copycat
            if len(self.raw_moves) >= 1:
                return self.store(self.raw_moves[len(self.raw_moves)-1][1])
        return self.store(True)