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
    if bot.storage["pending_user"][user_id] == "2":
        content = discord.Embed(
            title = "Please Choose your degree",
            description = "Please select the reaction to represent your degree",
            colour = discord.Colour.orange()
        )

        fields_mapper = {
            "⚙": "Phd",
            "💻": "Master",
            "📜": "Bachelor",

        }
        for key, item in fields_mapper.items():
            content.add_field(name=item, value=key,inline=True)

        sent_message = await message.author.send(embed = content)

        for key in fields_mapper.keys():
            await sent_message.add_reaction(key)

        reaction = await api.wait_for_reaction(user_id)
        await sent_message.delete()
        response = fields_mapper['{}'.format(reaction)]
        print(reaction, response)

        DB().update_user_by_ID(message.author.id, {
            "prog_deg": response
        })
        bot.storage["pending_user"][user_id] = "3"
        transaction.commit()

      
