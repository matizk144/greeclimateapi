import socket
import asyncio
import json


class _udpClientProtocol(asyncio.DatagramProtocol):
    def __init__(self, message, loop):
        self.message = message
        self.transport = None
        self.loop = loop
        self.received_data = asyncio.Future()

    def connection_made(self, transport):
        self.transport = transport
        transport.sendto(self.message)

    def datagram_received(self, data, addr):
        received_message = data
        self.received_data.set_result(received_message)
        self.transport.close()

    def connection_lost(self, exc):
        if not self.received_data.done():
            # If the connection is lost before receiving data, set the result to None
            self.received_data.set_result(None)


class greeDeviceConnection:
    def __init__(self, device_ip):
        self.deviceIp = device_ip

    async def send_data(self, request):
        tries_count = 0
        while tries_count < 10:
            try:
                data = await self._send_udp_message(bytes(request, "ascii"))
                return json.loads(data)
            except:
                tries_count = tries_count + 1
                await asyncio.sleep(1)
        raise Exception("Cannot communicate with climate")

    async def _send_udp_message(self, message):
        loop = asyncio.get_running_loop()
        transport, protocol = await loop.create_datagram_endpoint(
            lambda: _udpClientProtocol(message, loop),
            remote_addr=(self.deviceIp, 7000)
        )

        try:
            result = await asyncio.wait_for(protocol.received_data, 0.5)
            return result
        finally:
            transport.close()
