"""This bot always cheats. """

from bot_class import Bot
    
class AlwaysCheatBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'always_cheat')
        
    def move(self, bot_list):
        return False
