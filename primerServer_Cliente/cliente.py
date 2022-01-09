import asyncio
import websockets

numeros=['1', '2', '3', '4', '5', '6', '7', '8']

async def cliente(uri):
    async with websockets.connect("ws://localhost:8765") as ws:
        for numero in numeros:
            await ws.send("Contando: " + numero)
            await asyncio.sleep(0.5)
            respuesta = await ws.recv()
            print("ECHO CLIENT:", respuesta)


asyncio.run(cliente("ws://localhost:8765"))