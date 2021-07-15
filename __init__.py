from Bot import Bot
from IntroductionBot import page6
from BotStorage import BotStorage
import transaction

class IntroductionBot(Bot):
    def __init__(self) -> None:
        super().__init__()
        self.storage = BotStorage(self)
        if self.storage["pending_users"] == None:
            self.storage["pending_users"] = {}

    async def on_ready(self):
        print("IntroductionBot ready") # FIXME:

    async def on_message(self, message):
        await page6.on_message(self, message)
    
    async def on_bot_message(self, message):
        await page6.on_bot_message(self, message)

    async def on_member_join(self, member):
        self.storage["pending_users"][member.id] = {
            "name": member.name,
            "current_page": "6" # FIXME:
        }
        transaction.commit()
