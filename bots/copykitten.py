from bots.bot_class import Bot
    
class CopyKittenBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'copykitten')

    def move(self):
        if self.raw_moves:
            if len(self.raw_moves) >= 2:
                return self.raw_moves[-1][1] or self.raw_moves[-2][1]
        return True
