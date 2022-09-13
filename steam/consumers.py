from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class StreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.stream_key = self.scope['url_route']['kwargs']['stream_key']
        await self.channel_layer.group_add(self.stream_key, self.channel_name)
        await self.accept()
    
    async def disconnect(self):
        await self.channel_layer.group_discard(self.stream_key, self.channel_name)

    async def reload(self, event):
        output = event['output']

        await self.send(output)