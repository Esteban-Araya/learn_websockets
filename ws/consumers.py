from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
from channels.consumer import AsyncConsumer
import json
import asyncio
from random import randint
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        # Agregamos al consumidor al grupo "chat" usando el channel_layer.
        await self.channel_layer.group_add(self.scope["url_route"]["kwargs"]["pk"], self.channel_name)
        
        # Aceptamos la conexión WebSocket.
        await self.accept()
        # Obtenemos el usuario asociado a la conexión actual.
        client = self.scope["client"]
        
        # Enviamos un mensaje de bienvenida al usuario que se conectó.

    async def disconnect(self, close_code):
        # Eliminamos al consumidor del grupo self.scope["url_route"]["kwargs"]["pk"] usando el channel_layer.
        await self.channel_layer.group_discard(self.scope["url_route"]["kwargs"]["pk"], self.channel_name)

    async def receive(self, text_data):
        # Enviamos el mensaje recibido a todos los consumidores en el grupo self.scope["url_route"]["kwargs"]["pk"] usando el channel_layer.
        await self.channel_layer.group_send(
            self.scope["url_route"]["kwargs"]["pk"],
            {
                "type": "chat.message",
                "text": text_data,
                "client": self.scope["client"][1]
            }
        )
        

    async def chat_message(self, event):
        # Enviamos el mensaje recibido de vuelta al cliente actual a través del WebSocket.
        
        if event["client"] == self.scope["client"][1]:
            return

        await self.send(text_data=event["text"])


class randomNum(AsyncWebsocketConsumer):
    

    async def connect(self):
        await self.accept()

        for i in range(100):
            await self.send(json.dumps({"message": randint(0,101)}))
            await asyncio.sleep(5)
   
        await self.close()
        

    async def disconnect(self, close_code):
        
        
        await self.close()
    

