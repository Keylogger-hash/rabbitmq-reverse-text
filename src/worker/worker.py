import aio_pika
from aio_pika.abc import AbstractIncomingMessage
import asyncio
from rabbitmq_service import publisher
import config
import json


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        text = message.body.decode("utf-8")
        reverse_message = text[::-1]
        content = json.dumps({"input": text, "output": reverse_message}, ensure_ascii=False)
        print(f"Received message {reverse_message!r}")
        await publisher.publish(config.rabbitmq_url, config.worker_queue_results, content)
        # print(f"Message body is: {reverse_message.body!r}")


async def background_worker():
    print(config.rabbitmq_url)
    connection = await aio_pika.connect_robust(config.rabbitmq_url)
    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        queue = await channel.declare_queue(config.worker_queue, durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                await process_message(message)


async def main():
    worker_task = asyncio.create_task(background_worker())
    await worker_task


if __name__ == "__main__":
    asyncio.run(main())
