"""This bot always cooperates. """

from bots.bot_class import Bot
    
class AlwaysCooperateBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'always_cooperate')
        
    def move(self, bot_list):
        return True
