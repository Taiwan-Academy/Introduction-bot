from Bot import Bot
import json
from API import API
from os import listdir
from os.path import isfile, join
class IntroductionBot(Bot):

    def __init__(self):
        super().__init__()
        # print("Intro init")

        # KEY, submod
        # mypath = '.'
        # onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        # print(onlyfiles)

        # Loads Page Configure JSON
        f = open('./IntroductionBot/configure.json')
        self.pages = json.load(f)
        f.close()

    def on_ready(self):
        print("IntroductionBot ready") # FIXME:

    def on_message(self, message):
        print("IntroductionBot message: [{}] {}".format(message.author, message.content)) # FIXME:
        message = self.api.client_await()
        print("Client_await {}".format(message))
    
    # def on_member_join(self, member):
    #     Pages = self.pages['pages']
    #     for page in Pages:
    #         print(page)

    #     print('')
