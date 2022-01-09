import asyncio
import websockets


async def echo(echoserver, path):
    mensage = await echoserver.recv()
    await echoserver.send(mensage)
    await asyncio.sleep(0.5)
    print("ECHO SERVER: recibe y envia [mensage]: [", mensage, "]")


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()


