# WebSockets

Libreria con la que podemos crear clientes y servidores [WebSockets](https://pypi.org/project/websockets/) en python.

Construdia por encima de *asyncio* [WebSockets](https://websockets.readthedocs.io/en/stable/index.html) nos brinda una manera mas simple de trabajar con **CoRutinas**.

Don’t worry about the opening and closing handshakes, pings and pongs, or any other behavior described in the specification. websockets takes care of this under the hood so you can focus on your application!

Also, websockets provides an interactive client:

`python -m websockets ws://localhost:8765/`

### Why shouldn’t I use websockets?

If you prefer callbacks over coroutines: websockets was created to provide the best coroutine-based API to manage WebSocket connections in Python. Pick another library for a callback-based API.


## Notas sobre cambios en las versiones

Websockets v9.1 is the last version supporting Python 3.6, donde las coRutinas requieren 2 parametros como vemos en el siguiente ejemplo

```
async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)
```

Websockets > v10 que estan a partir de python > 3.8

En cambio aqui el path lo obtiene como una propiedad mas del objeto websocket.path

```
async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
```


## Guia de ejemplos con los que desarrolle el aprendizaje

El primer ejercicio un poco fjorzado por el cambio de version y otro poco para entender mas acerca de los *LOOP* fue contruir un Cliente/Servidor para que hagan un ECHO de dos formas distientas:

- loopControl
- primerServer_Cliente

Ambas tienen la estructura basica de un websocket, inclusive dentro de loopControl mostramos como poner la *corutina echo* en un **for loop** para que permanentemente este atenta a si llegan msg nuevos.

No confundir el *for loop* de la corutina con el **main loop** de la aplicacion.


Otra parte importante es:

```
async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

```

`asyncio.Future()` are needed to allow callback-based code to be used with async/await.

Por otra parte es interesante correr el server y 2 clientes al mismo tiempo para entender que websocket server executes the handler coroutine echoServer() once for each cliente connection. 
