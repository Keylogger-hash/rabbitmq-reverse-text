from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
from rabbitmq_service.subscriber import subscribe
import config
import asyncio
import json


app = FastAPI()


@app.get("/")
async def index():
    return "ok"


@app.websocket("/listen_results")
async def listen_results_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await subscribe(config.rabbitmq_url, config.worker_queue_results)
        await websocket.send_text(data)
        await asyncio.sleep(1)


if __name__ == "__main__":
    uvicorn.run("websocket_api:app", reload=True, host="0.0.0.0", port=8001, log_level="debug")
