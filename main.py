from fastapi import FastAPI
from publisher import publish
import asyncio
import uvicorn
app = FastAPI()

@app.get("/")
async def index():
    return "ok"

@app.post("/queue_reverse_text")
async def reverse_text_route(text: str):
    await publish(text)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)