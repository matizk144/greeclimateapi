import socket
import base64
import json
import time

from Crypto.Cipher import AES


class greeDeviceConnection:
    def __init__(self, device_ip):
        self.deviceIp = device_ip

    def send_data(self, request):
        tries_count = 0
        client: socket = None
        while tries_count < 10:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                client.settimeout(0.5)
                client.sendto(bytes(request, "ascii"), (self.deviceIp, 7000))
                data, addr = client.recvfrom(64000)
                return json.loads(data)
            except:
                tries_count = tries_count + 1
                time.sleep(1)
            finally:
                client.close()
        raise Exception("Cannot communicate with climate")


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
