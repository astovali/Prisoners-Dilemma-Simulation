"""This is a sample bot, to show how to do such a thing."""

#Disclaimer: the bot_list is in the format
#[bot_1, bot_2]
#Check the name to see which is which, we will never do mirror matches.

from bots.bot_class import Bot
    
class SampleBot(Bot):
    def __init__(self):
        Bot.__init__(self, 'sample_bot') #replace the name with your bot's name

    def move(self):
        #do some stuff

        #format: cooperate is True, cheat is False
        return None
