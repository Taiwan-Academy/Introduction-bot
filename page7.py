import discord
import transaction
from datetime import datetime
import sys
sys.path.append("..")
from API import API
from DB import DB

async def on_message(bot, message):
    user_id = str(message.author.id)
    if bot.storage["pending_user"][user_id] == "7":
        api = API()
        content = discord.Embed(
            title = "Thank you for your patience, Welcome Joining 台灣學棧",
            description = "Now you should able to see the channels in the server, if encounter any difficulties please contact xxxx",
            colour = discord.Colour.orange()
        )
        guild = 741527808400031854 # brian86258 的伺服器
        await message.author.send(embed = content)
        role_id = 849863921765842954 # NOTE still need to change, this id is reserved for the role_id for role: 'verified'
        await api.add_role(message.author, role_id, guild)
        

        # del pendin_user, and update such user into validated_user
        del bot.storage["pending_user"][user_id]
        bot.storage["validated_user"].append(user_id)
        transaction.commit()
        # Change User status to verified
        DB().update_user_by_ID(message.author.id, {
            "user_status": "Verified",
            "last_updated_dt": datetime.now()
            }
        )