from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )        
        self.accept()
        self.send(text_data=json.dumps(
            {
                "message": "you are connected from test consumer!!"
            }
        ))

    def receive(self, text_data): # when we receive data from client
        print(text_data)
        self.send(text_data=json.dumps(
            {  
                "message": text_data    
            }
        ))

    def disconnect(self, close_code):
        print("disconnected")

    def send_notification(self, event):
        print(event)
        self.send(event["value"])
        print("notification sent")
