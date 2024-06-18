import mitmproxy.http
from mitmproxy import ctx
import asyncio
import websockets

class GetMsg:
    def __init__(self):
        self.clients = set()
        # Schedule the start of the WebSocket server in the running event loop
        asyncio.ensure_future(self.start_server())

    async def start_server(self):
        server = await websockets.serve(self.handler, '0.0.0.0', 8082)
        ctx.log.info("WebSocket server started at ws://localhost:8082")
        await server.wait_closed()

    async def handler(self, websocket, path):
        self.clients.add(websocket)
        ctx.log.info(f"Client connected: {websocket.remote_address}")
        try:
            async for message in websocket:
                print(f"Received message from client: {message}")
                # 将message返回给客户端
                await self.send_to_clients(message)
        finally:
            self.clients.remove(websocket)
            ctx.log.info(f"Client disconnected: {websocket.remote_address}")

    async def send_to_clients(self, message):
        print(f"Sending message to {len(self.clients)} clients")
        print(self.clients)
        if self.clients:
            await asyncio.wait([asyncio.create_task(client.send(message)) for client in self.clients])

    def request(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info('Request URL: {}'.format(flow.request.url))

    def websocket_message(self, flow: mitmproxy.http.HTTPFlow):
        message = flow.websocket.messages[-1].content.decode('utf-8', 'ignore')
        # 如果message中包含market，就发送给客户端
        if 'gmName' in message:
            ctx.log.warn(f"WebSocket message: { message}")
            asyncio.ensure_future(self.send_to_clients(message))
addons = [
    GetMsg()
]
