import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """
        사용자와 WebSocket 연결이 맺어졌을 때 호출
        """
        user = self.scope["user"]

        if user.is_authenticated:
            username = user.username 
        else:
            username = "hihi"
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """
        사용자와 WebSocket 연결이 끊겼을 때 호출
        """
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        """
        사용자가 메세지를 보낼 떄 호출
        """
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # 사용자 정보 추가
        user = self.scope["user"]

        if user.is_authenticated:
            username = user.username 
        else:
            username = "hihi"
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "username":username, "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        user = self.scope["user"]

        if user.is_authenticated:
            username = user.username 
        else:
            username = "hihi"
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"username":username,"message": message}))

        
