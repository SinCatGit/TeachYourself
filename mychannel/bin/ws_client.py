#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json


async def hello():
    uri = "ws://127.0.0.1:8000/ws/chat/hobby/"
    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        greeting = json.loads(greeting)
        print(f"< {greeting['message']}")

asyncio.get_event_loop().run_until_complete(hello())
