import discord
import transaction
import re
from datetime import datetime
from DB import DB

date_re = re.compile(r"\d\d\d\d-\d\d-\d\d")

async def on_message(bot, message):
    user_id = str(message.author.id)
    if bot.storage["pending_user"][user_id] == "5":
        content = discord.Embed(
            title = "Please input your program name",
            description = "Input the program name when you study in America",
            colour = discord.Colour.orange()
        )
        await message.author.send(embed = content)
        bot.storage["pending_user"][user_id] = "5-1"
        transaction.commit()
    elif bot.storage["pending_user"][user_id] == "5-1":
        DB().update_user_by_ID(message.author.id, {
            "prog_name": message.content
        })
        content = discord.Embed(
            title = "Thank you. Please input your program start date",
            description = "Input program start date in format yyyy-mm-dd (Example: 2021-09-20)",
            colour = discord.Colour.orange()
        )
        await message.author.send(embed = content)
        bot.storage["pending_user"][user_id] = "5-2"
        transaction.commit()
    elif bot.storage["pending_user"][user_id] == "5-2":
        if date_re.match(message.content) != None:
            DB().update_user_by_ID(message.author.id, {
                "prog_start_yr": datetime.strptime(message.content, '%Y-%m-%d')
            })
            content = discord.Embed(
                title = "Please input your program end date",
                description = "Input program end date in format yyyy-mm-dd (Example: 2021-09-20)",
                colour = discord.Colour.orange()
            )
            await message.author.send(embed = content)
            bot.storage["pending_user"][user_id] = "5-3"
            transaction.commit()
        else:
            content = discord.Embed(
                title = "Invalid format! Please input your program start date again",
                description = "Input program start date in format yyyy-mm-dd (Example: 2021-09-20)",
                colour = discord.Colour.red()
            )
            await message.author.send(embed = content)
    elif bot.storage["pending_user"][user_id] == "5-3":
        if date_re.match(message.content) != None:
            DB().update_user_by_ID(message.author.id, {
                "prog_end_yr": datetime.strptime(message.content, '%Y-%m-%d')
            })
            bot.storage["pending_user"][user_id] = "6"
            transaction.commit()
        else:
            content = discord.Embed(
                title = "Invalid format! Please input your program end date again",
                description = "Input program start date in format yyyy-mm-dd (Example: 2021-09-20)",
                colour = discord.Colour.red()
            )
            await message.author.send(embed = content)
