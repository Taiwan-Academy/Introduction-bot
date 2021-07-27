import discord
import transaction
import re
from datetime import datetime
from DB import DB
from API import API

async def on_message(bot, message):
    user_id = str(message.author.id)
    db = DB()
    api = API()
    if bot.storage["pending_user"][user_id] == "1":
        content = discord.Embed(
            title = "Welcome Join 台灣學棧",
            description = "Following are some steps to verify you as user, pleas be patient and thanks!",
            colour = discord.Colour.orange()
        )
        await message.author.send(embed = content)
        bot.storage["pending_user"][user_id] = "2"
        transaction.commit()

      
