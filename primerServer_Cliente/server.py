import asyncio
import websockets


async def echo(echoserver):
    try:
        async for msg in echoserver:
            await echoserver.send(msg)
            await asyncio.sleep(0.5)
            print("ECHO SERVER: recibe y envia [mensage]: [", msg, "]")

    except websockets.ConnectionClosedOK:
        print("Conn closed")


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()


asyncio.run(main())
