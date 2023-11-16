from bots.bot_class import Bot
    
class CopyCatBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'copycat')

    def move(self):
        if self.raw_moves:
            return self.raw_moves[len(self.raw_moves)-1][1]
        return True
