import transaction
from Bot import Bot
from BotStorage import BotStorage
from BTrees.OOBTree import OOBTree
from persistent.list import PersistentList
from DB import DB
from IntroductionBot import page5, page6

class IntroductionBot(Bot):
    def __init__(self) -> None:
        super().__init__()
        self.storage = BotStorage(self)
        if self.storage["pending_user"] == None:
            self.storage["pending_user"] = OOBTree()
        if self.storage["validated_user"] == None:
            self.storage["validated_user"] = PersistentList()

    async def on_ready(self):
        print("IntroductionBot ready")

    async def on_message(self, message):
        await page5.on_message(self, message)
        await page6.on_message(self, message)

    async def on_member_join(self, member):
        DB().add_users({
            "user_id": member.id,
            "user_name": f"{member.name}#{member.discriminator}"
        })
        self.storage["pending_user"][str(member.id)] = "5" # FIXME:
        transaction.commit()
