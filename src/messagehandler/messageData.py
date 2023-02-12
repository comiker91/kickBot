import json


class Message(object):

    def __init__(self, websocketmessage:dict) -> None:

        self.messagecontent = None
        
        # Base websocketmessage
        self.websocketmessage = websocketmessage

        # websocket events
        self.event = self.websocketmessage["event"]

        if self.event == "pusher:connection_established":
            return
        
        if self.event == "pusher_internal:subscription_succeeded":
            return

        # base data
        self.data = json.loads(self.websocketmessage["data"])

        # base message data
        self.message = self.data["message"]

        # message id
        self.messageID = self.message["id"]

        # message content
        self.messagecontent = self.message["message"]

        # message sender role
        self.role = self.message["role"]
        if self.role == "Channel Host":
            self.isMod = True
        elif self.role == "Moderator":
            self.isMod = True
        else:
            self.isMod = False

        # Informations
        self.chatroom_id = self.message["chatroom_id"]
        self.created_at = self.message["created_at"]
        
        # UNUSED
        self.type = self.message["type"]
        self.replied_to = self.message["replied_to"]
        self.is_info = self.message["is_info"]
        self.link_preview = self.message["link_preview"]
        self.optional_message = self.message["optional_message"]
