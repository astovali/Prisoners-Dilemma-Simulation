from bots.bot_class import Bot
from random import random
    
class RandomBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'random')
        
    def move(self, other):
        return bool(round(random()))
