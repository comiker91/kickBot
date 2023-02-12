from .messageData import Message

class Commands(object):

    def __init__(self, message: Message) -> None:
        self.isMod = message.isMod
        self.message = message.messagecontent

        if self.message.lower() == "!discord":
            self.discord()

    def discord(self):
        print("DISCORD")
    