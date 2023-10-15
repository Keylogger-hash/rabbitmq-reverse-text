import aio_pika


async def subscribe(rabbitmq_url:str, queue_name: str):
    connection = await aio_pika.connect_robust(
        rabbitmq_url
    )
    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        queue = await channel.declare_queue(
            queue_name, durable=True
        )
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    return message.body.decode()
