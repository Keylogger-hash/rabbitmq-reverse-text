import websockets
import asyncio
import json

url = "ws://localhost:8001/listen_results"


async def listen_results():

    async for websocket in websockets.connect(url):
        try:
            while True:
                data = await asyncio.wait_for(websocket.recv(), timeout=100)
                json_data = json.loads(data)
                input_message = json_data.get('input')
                output_message = json_data.get('output')
                print(f"input: {input_message} output: {output_message}")
                await asyncio.sleep(2)
        except websockets.ConnectionClosed:
            continue

if __name__ == "__main__":

    asyncio.run(listen_results())
