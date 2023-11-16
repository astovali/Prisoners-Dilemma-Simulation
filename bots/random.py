from bots.bot_class import Bot
from random import random
    
class RandomBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'random')
        
    def move(self):
        return bool(round(random()))
