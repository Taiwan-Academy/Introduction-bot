from Bot import Bot
from IntroductionBot import page6

class IntroductionBot(Bot):
    
    def on_ready(self):
        print("IntroductionBot ready") # FIXME:

    async def on_message(self, message):
        await page6.on_message(self, message)