import discord
import transaction
import sys
from IntroductionBot import page7

sys.path.append("..")
from DB import DB

async def on_message(bot, message):
    if message.author.id in bot.storage["pending_users"].keys():
        user = bot.storage["pending_users"][message.author.id]
        db = DB()
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
            linkedin_url = message.content
            # Verify linkedin url, if fail break
            
            print("Page 6 User: {}, Link {}".format(user, linkedin_url)) # FIXME:
            user_info = {
                'linkedin_url' : linkedin_url,
            }
            res = db.update_user_by_ID(message.author.id, user_info)
            # update current_page
            user["current_page"] = "7"
            transaction.commit()

            # Call page to send Thank you page
            if res == 1: # if successful update user, then send thank you page
                page7.send_page_and_verified(bot,message)