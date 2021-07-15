import discord
import transaction
import sys
sys.path.append("..")
from API import API

async def send_page_and_verified(bot, message):
    if message.author.id in bot.storage["pending_users"].keys():
        user = bot.storage["pending_users"][message.author.id]
        api = API()

        content = discord.Embed(
            title = "Thank you for your patience, Welcome Joining 台灣學棧",
            description = "Now you should able to see the channels in the server, if encounter any difficulties please contac xxxx",
            colour = discord.Colour.orange()
        )
        await message.author.send(embed = content)
        role_id = 849863921765842954 # NOTE still need to change, this id is reserved for the role_id for role: 'verified'
        await api.add_role(message.author, role_id)
        # Final update the user's current_page?
        # user["current_page"] = "-1"
        # transaction.commit()


    