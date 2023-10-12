import aio_pika
from aio_pika.abc import AbstractIncomingMessage
import asyncio
from aio_pika import DeliveryMode, Message, connect


async def publish(text: str):
    connection = await aio_pika.connect("amqp://guest:guest@localhost:5672/")
    async with connection:
        channel = await connection.channel()
        print(type(text))
        message_body = text.encode('utf-8')

        message = Message(
            message_body, delivery_mode=DeliveryMode.PERSISTENT,
        )
        await channel.default_exchange.publish(
            message, routing_key="reverse_text_queue"
        )
        await asyncio.sleep(1)


# async def main():
#     worker_task = asyncio.create_task(publisher("message"))
#     await worker_task
#
# if __name__ == "__main__":
#     asyncio.run(main())