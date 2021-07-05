from discord import message


account_status = "page6" #FIXME: Should retrieve from DB

def on_message(bot, message):
    global account_status
    if account_status == "page6":
        user = message.author
        linkin_link = message.content
        account_status = "page7"
        print("Page 6 User: {}, Link {}".format(user, linkin_link)) # FIXME: