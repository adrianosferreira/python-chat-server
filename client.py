import asyncio
import websockets


async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send('something')


asyncio.get_event_loop().run_until_complete(main())
