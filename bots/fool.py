from bots.bot_class import Bot
    
class FoolBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'fool')

    def move(self, other):
        if self.raw_moves:
            if len(self.raw_moves) >= 2:
                if self.raw_moves[len(self.raw_moves)-1][1]:
                    return self.raw_moves[len(self.raw_moves)-1][0]
                else:
                    return not self.raw_moves[len(self.raw_moves)-1][0]
        return True
