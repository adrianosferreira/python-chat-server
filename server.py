import asyncio
import websockets
import json

USERS = set()


async def register(websocket):
    USERS.add(websocket)


async def unregister(websocket):
    USERS.remove(websocket)


async def notify_users(msg):
    if USERS:
        await asyncio.wait([ws.send(json.dumps(msg)) for ws in USERS])


async def chat(websocket, path):
    await register(websocket)
    try:
        async for msg in websocket:
            data = json.loads(msg)
            print(data)
            await notify_users(data)

    finally:
        await unregister(websocket)


start_server = websockets.serve(chat, "localhost", 3000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
