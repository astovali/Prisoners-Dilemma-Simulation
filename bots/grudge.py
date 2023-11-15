from bots.bot_class import Bot
    
class GrudgeBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'grudge')
        self.angry = False
    
    def reset(self, hard=False):
        Bot.reset(self, hard=hard)
        self.angry = False

    def move(self, other):
        if self.angry:
            return False
        if self.raw_moves:
            if self.raw_moves[len(self.raw_moves)-1][1] == False:
                self.angry = True
                return False
        return True
