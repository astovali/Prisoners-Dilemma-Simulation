"""This code outlines a bot class and some basic functionality"""

class Bot:
    def __init__(self, name):
        self.name = name
        self.cooperate_num = 0 #the amount of times the bot cooperated
        self.cheat_num = 0 #the amount of times the bot cheated
        self.raw_moves = [] #all the moves, raw, in order
        self.score = 0 #total score
    
    def update(self, move, score):
        self.cooperate_num += move
        self.cheat_num += not move
        self.raw_moves.append(move)
        self.score += score

    def __str__(self):
        return f'''Name = {self.name},
Amount of cooperates = {self.cooperate_num}, 
Amount of cheats = {self.cheat_num}, 
Raw moves = {self.raw_moves}, 
Current score = {self.score}.
'''

    def reset(self):
        self.cooperate_num = 0
        self.cheat_num = 0
        self.raw_moves = []
        self.score = 0
   
