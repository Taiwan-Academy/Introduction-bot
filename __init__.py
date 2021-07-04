from Bot import Bot
import json
from API import API
api = API()

class IntroductionBot(Bot):
    def __init__(self):
        super().__init__()

        # Loads Page Configure JSON
        f = open('configure.json')
        self.pages = json.load(f)
        f.close()

    def on_ready(self):
        print("IntroductionBot ready") # FIXME:

    def on_message(self, message):
        print("IntroductionBot message: [{}] {}".format(message.author, message.content)) # FIXME:
        message = api.client_await()
        print(message)
    
    def on_member_join(self, member):
        Pages = self.pages['pages']
        for page in Pages:
            print(page)

        print('')