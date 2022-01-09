import asyncio
import websockets


async def echo(echoserver):
    try:
        mensage = await echoserver.recv()
        await echoserver.send(mensage)
        await asyncio.sleep(0.5)
        print("ECHO SERVER: recibe y envia [mensage]: [", mensage, "]")

    except websockets.ConnectionClosedOK:
        print("Conn closed")


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()


asyncio.run(main())
