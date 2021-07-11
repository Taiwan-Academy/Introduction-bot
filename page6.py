import discord

account_status = "page5" #FIXME: Should retrieve from DB

async def on_message(bot, message):
    global account_status
    if account_status == "page5":
        content = discord.Embed(
            title = "[Optioal] Please input your LinkedIn link",
            description = "Input the link of your LinkedIn profile page if you wish.",
            colour = discord.Colour.orange()
        )
        await message.author.send(embed = content)
        account_status = "page6"
    elif account_status == "page6":
        user = message.author
        linkin_link = message.content
        print("Page 6 User: {}, Link {}".format(user, linkin_link)) # FIXME: