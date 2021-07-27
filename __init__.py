import discord
import transaction
from Bot import Bot
from BotStorage import BotStorage
from BTrees.OOBTree import OOBTree
from persistent.list import PersistentList
from DB import DB
from IntroductionBot import page1,page2,page3, page4 ,page5, page6, page7


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
        self.__ensure_user(message.author)
        if not message.author.bot:
            await page1.on_message(self, message)
            await page2.on_message(self, message)
            await page3.on_message(self, message)
            await page4.on_message(self, message)
            await page5.on_message(self, message)
            await page6.on_message(self, message)
            await page7.on_message(self, message)


    async def on_member_join(self, member):
        if not member.bot:
            self.__ensure_user(member)

    async def on_member_update(self, before, member):
        if (
            (not member.bot)
            and (not (str(member.id) in self.storage["validated_user"]))
            and (member.status != before.status)
            and (member.status == discord.Status.online)
        ):
            self.__ensure_user(member)
            await member.send(embed = discord.Embed(
                title = "Account not verified",
                description = "Please input anything to finish introduction questions",
                colour = discord.Colour.red()
            ))

    def __ensure_user(self, user):
        db = DB()
        if db.get_user_by_ID(user.id) == None:
            db.add_users({
                "user_id": user.id,
                "user_name": f"{user.name}#{user.discriminator}"
            })

        if not self.storage["pending_user"].has_key(str(user.id)):
            self.storage["pending_user"][str(user.id)] = "7" # FIXME:
            transaction.commit()
