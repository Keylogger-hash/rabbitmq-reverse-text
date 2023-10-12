import aio_pika
from aio_pika.abc import AbstractIncomingMessage
import asyncio


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        text = message.body.decode('utf-8')
        reverse_message = text[::-1]
        print(f" [x] Received message {reverse_message!r}")
        # print(f"Message body is: {reverse_message.body!r}")


async def background_worker():
    while True:
        connection = await aio_pika.connect("amqp://guest:guest@localhost:5672/")
        async with connection:
            channel = await connection.channel()
            await channel.set_qos(prefetch_count=1)

            queue = await channel.declare_queue(
                "reverse_text_queue",
                durable=True
            )
            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    await process_message(message)

async def main():
    worker_task = asyncio.create_task(background_worker())
    await worker_task
if __name__ == "__main__":
    asyncio.run(main())