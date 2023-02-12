import json
import websocket
from src.messagehandler.messageData import Message
from src.messagehandler.commands import Commands


class BaseClient(object):

    def __init__(self)->None:
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(url="wss://ws-us2.pusher.com/app/eb1d5f283081a78b932c?protocol=7&client=js&version=7.4.0&flash=false",
                                    on_open=self.on_open,
                                    on_close=self.on_close,
                                    on_ping=self.on_ping,
                                    on_error=self.on_error,
                                    on_message=self.on_message)
    
    def get_client(self):
        return self.ws



    def on_open(self, ws):
        ws.send(json.dumps(
            {
                "event": "pusher:subscribe",
                "data": {
                    "auth": "",
                    "channel": "chatrooms.214448"
                }
            }
        ))

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")

    def on_ping(self, ws, message):
        print("Pong was send")

    def on_error(self, ws, error):
        print(error)

    def on_message(self, ws, message):
        message = json.loads(message)
        message = Message(message)
        if message.messagecontent is not None:
            Commands(message=message)
        





