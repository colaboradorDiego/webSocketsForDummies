# WebSockets

Libreria con la que podemos crear clientes y servidores [WebSockets](https://pypi.org/project/websockets/) en python.

Construdia por encima de *asyncio* [WebSockets](https://websockets.readthedocs.io/en/stable/index.html) nos brinda una manera mas simple de trabajar con **CoRutinas**.

Don’t worry about the opening and closing handshakes, pings and pongs, or any other behavior described in the specification. websockets takes care of this under the hood so you can focus on your application!

Also, websockets provides an interactive client:

`python -m websockets ws://localhost:8765/`

A continuacion detallamos las caractetisticas mas importantes en este punto a tener un cuenta.

- Websocket server executes the handler coroutine echoServer() once for each cliente connection. 
- onOpen, onMessage, onError, and onClose **son CoRutinas!!! NO SON callBacks**?


## Notas sobre cambios en las versiones

Websockets v9.1 is the last version supporting Python 3.6, donde las coRutinas requieren 2 parametros como vemos en el siguiente ejemplo

```
async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)
```

Websockets > v10

En cambio aqui el path lo obtiene como una propiedad mas del objeto websocket.path

```
async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
```


	
