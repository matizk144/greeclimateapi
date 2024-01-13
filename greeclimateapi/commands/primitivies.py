import socket
import asyncio
import base64
import json
import time

from Crypto.Cipher import AES


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


class greeDeviceCipher:
    def __init__(self):
        self.genericDeviceKey = "a3K8Bx%2r8Y7#xDh"
        self.cipher = AES.new(self.genericDeviceKey.encode("utf-8"), AES.MODE_ECB)

    def encode(self, data_in_string):
        data_in_bytes = self.pad(data_in_string).encode("utf-8")
        encrypted_data = self.cipher.encrypt(data_in_bytes)
        base64encoded = base64.b64encode(encrypted_data)
        return base64encoded.decode("utf-8")

    def decode(self, data_in_base64):
        base64decoded = base64.b64decode(data_in_base64)
        decrypted_data = self.cipher.decrypt(base64decoded)
        decrypted_data_str = decrypted_data.decode("utf-8")
        decrypted_data_str_trimmed = decrypted_data_str.replace('\x0f', '').replace(
            decrypted_data_str[decrypted_data_str.rindex('}') + 1:], '')
        return json.loads(decrypted_data_str_trimmed)

    @staticmethod
    def pad(s):
        aes_block_size = 16
        return s + (aes_block_size - len(s) % aes_block_size) * chr(aes_block_size - len(s) % aes_block_size)

    def set_key(self, key):
        self.cipher = AES.new(key.encode("utf-8"), AES.MODE_ECB)
