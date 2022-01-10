import asyncio
import websockets


async def echo(echoserver, path):
    try:
        async for msg in echoserver:
            await echoserver.send(msg)
            await asyncio.sleep(0.5)
            print("ECHO SERVER: recibe y envia [mensage]: [", msg, "]")

    except websockets.ConnectionClosedOK:
        print("Conn closed")


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


loop = asyncio.new_event_loop()
try:
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
finally:
    loop.close()
