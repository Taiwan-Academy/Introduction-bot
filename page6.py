import discord
import transaction
import re
from DB import DB

linkedin_re = re.compile(r"(https|http)://(www.linkedin.com|linkedin.com)/in/.*")

async def on_message(bot, message):
    user_id = str(message.author.id)
    if bot.storage["pending_user"][user_id] == "6":
        content = discord.Embed(
            title = "Please input your LinkedIn link",
            description = "Input the link of your LinkedIn profile page, or N/A if you don't wish to provide",
            colour = discord.Colour.orange()
        )
        await message.author.send(embed = content)
        bot.storage["pending_user"][user_id] = "6-1"
        transaction.commit()
    elif bot.storage["pending_user"][user_id] == "6-1":
        if (message.content == "N/A") or (linkedin_re.match(message.content) != None):
            DB().update_user_by_ID(message.author.id, {
                "linkedin_url": message.content
            })
            bot.storage["pending_user"][user_id] = "7"
            transaction.commit()
        else:
            content = discord.Embed(
                title = "Invalid format! Please input valid again",
                description = "Input the link of your LinkedIn profile page, or N/A if you don't wish to provide",
                colour = discord.Colour.red()
            )
            await message.author.send(embed = content)