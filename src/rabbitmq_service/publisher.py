import aio_pika
import asyncio
from aio_pika import DeliveryMode, Message


async def publish(rabbitmq_url: str, queue_name: str, text: str):
    connection = await aio_pika.connect(rabbitmq_url)
    async with connection:
        channel = await connection.channel()
        print(type(text))
        message_body = text.encode("utf-8")
        message = Message(
            message_body,
            delivery_mode=DeliveryMode.PERSISTENT,
        )
        await channel.default_exchange.publish(message, routing_key=queue_name)
        await asyncio.sleep(1)


# async def main():
#     worker_task = asyncio.create_task(publisher("message"))
#     await worker_task
#
# if __name__ == "__main__":
#     asyncio.run(main())
