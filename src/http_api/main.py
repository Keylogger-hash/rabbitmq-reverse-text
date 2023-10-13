from fastapi import FastAPI
from rabbitmq_service.publisher import publish
import uvicorn
import config

app = FastAPI()


@app.get("/")
async def index():
    return "ok"


@app.post("/queue_reverse_text")
async def reverse_text_route(text: str):
    await publish(config.rabbitmq_url, config.worker_queue, text)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
