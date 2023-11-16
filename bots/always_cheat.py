"""This bot always cheats. """

from bots.bot_class import Bot
    
class AlwaysCheatBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'always_cheat')
        
    def move(self):
        return False
