from fastapi import FastAPI, WebSocket
import uvicorn
# from subscriber import subscribe
import websockets
import aio_pika
from aio_pika.abc import AbstractIncomingMessage
import asyncio
from aio_pika import DeliveryMode, Message, connect, ExchangeType



app = FastAPI()

messages = []


async def on_message(message:AbstractIncomingMessage):
    messages.append(message)


async def subscribe():
    connection = await aio_pika.connect("amqp://guest:guest@localhost:5672/")
    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        queue = await channel.declare_queue(exclusive=True)
        exchange = await channel.declare_exchange(
            "logs", ExchangeType.FANOUT,
        )
        await queue.bind(exchange)
        await queue.consume(on_message)


@app.get("/")
async def index():
    return "ok"


@app.websocket("/listen_results")
async def listen_results_websocket(websocket:WebSocket):
    await websocket.accept()
    while True:
        await subscribe()
        #message = messages[-1]
        await websocket.send_text("message")


if __name__ == "__main__":
    uvicorn.run("websocket_api:app", reload=True, port=8001,log_level='debug')
