import discord
import transaction

async def on_message(bot, message):
    user = bot.storage["pending_users"][message.author.id]
    if user["current_page"] == "6":
        content = discord.Embed(
            title = "Please input your LinkedIn link",
            description = "Input the link of your LinkedIn profile page, or N/A if you don't wish to provide",
            colour = discord.Colour.orange()
        )
        await message.author.send(embed = content)
        user["current_page"] = "6-1"
        transaction.commit()
    elif user["current_page"] == "6-1":
        linkin_link = message.content
        print("Page 6 User: {}, Link {}".format(user, linkin_link)) # FIXME:
        user["current_page"] = "6"
        transaction.commit()