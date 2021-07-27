import discord
import transaction
from DB import DB

async def on_message(bot, message):
    user_id = str(message.author.id)

    db = DB()
    if bot.storage["pending_user"][user_id] == "3":
        content = discord.Embed(
            title = "Please input your School Name",
            description = "Input the abbreviation of your school name(Ex, CMU, NYU, UCI ...)",
            colour = discord.Colour.orange()
        )
        await message.author.send(embed = content)
        bot.storage["pending_user"][user_id] = "3-1"
        transaction.commit()
    elif bot.storage["pending_user"][user_id] == "3-1":
        univ_list = db.get_all_university()
        univ_abbrev_list = list(map(lambda x:x.univ_abbrev.upper(), univ_list))
        univ_abbrev_list.append("OTHER")
        msg = message.content.upper()
        if msg in univ_abbrev_list:
            DB().update_user_by_ID(message.author.id, {
                "univ_abbrev": msg
            })
            bot.storage["pending_user"][user_id] = "4"
            transaction.commit()
        else:
            content = discord.Embed(
                title = "Cannot find this School abbreviation!",
                description = "Sorry we cannot find this school abbreviation, please double check your input. Or typein other",
                # NOTE: future may be suggest potential inputs?
                colour = discord.Colour.red()
            )
            await message.author.send(embed = content)
