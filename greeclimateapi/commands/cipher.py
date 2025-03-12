import base64
import json

from Crypto.Cipher import AES
from abc import ABC, abstractmethod

class greeDeviceCipher(ABC):

    @abstractmethod
    def encrypt_pack_parameter(self, request, data_to_encrypt):
        pass

    @abstractmethod
    def decode_pack_parameter(self, response):
        pass

    @abstractmethod
    def decode(self, data_in_base64):
        pass
    @abstractmethod
    def set_key(self, key):
        pass

    @staticmethod
    def pad(s):
        aes_block_size = 16
        return s + (aes_block_size - len(s) % aes_block_size) * chr(aes_block_size - len(s) % aes_block_size)

class greeECBDeviceCipher(greeDeviceCipher):
    def __init__(self):
        self.cipher = AES.new("a3K8Bx%2r8Y7#xDh".encode("utf-8"), AES.MODE_ECB)

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

    def encrypt_pack_parameter(self, request, data_to_encrypt):
        request["pack"] = self.encode(str(data_to_encrypt).replace("'", '"'))
        return str(request).replace("'", '"')

    def decode_pack_parameter(self, response):
        decrypted_pack = self.decode(response["pack"])
        return decrypted_pack

    def set_key(self, key):
        self.cipher = AES.new(key.encode("utf-8"), AES.MODE_ECB)

class greeGCMDeviceCipher(greeDeviceCipher):
    def __init__(self):
        self.cipher : AES.GcmMode = None
        self.key = "{yxAHAY_Lm6pbC/<"

    def update(self):
        self.cipher = AES.new(self.key.encode("utf-8"), AES.MODE_GCM,
                              nonce=b'\x54\x40\x78\x44\x49\x67\x5a\x51\x6c\x5e\x63\x13')
        self.cipher.update(b'qualcomm-test')

    def encode_digest(self, data_in_string):
        data_in_bytes = self.pad(data_in_string).encode("utf-8")
        pack, tag = self.cipher.encrypt_and_digest(data_in_bytes)
        pack_base64encoded = base64.b64encode(pack).decode("utf-8")
        tag_base64encoded = base64.b64encode(tag).decode("utf-8")
        return pack_base64encoded, tag_base64encoded

    def decode(self, data_in_base64):
        base64decoded = base64.b64decode(data_in_base64)
        decrypted_data = self.cipher.decrypt(base64decoded)
        decrypted_data_str = decrypted_data.decode("utf-8")
        decrypted_data_str_trimmed = decrypted_data_str.replace('\x0f', '').replace(
            decrypted_data_str[decrypted_data_str.rindex('}') + 1:], '')
        return json.loads(decrypted_data_str_trimmed)

    def encrypt_pack_parameter(self, request, data_to_encrypt):
        self.update()
        pack, tag = self.encode_digest(str(data_to_encrypt).replace("'", '"'))
        request["pack"] = pack
        request["tag"] = tag
        return str(request).replace("'", '"')

    def decode_pack_parameter(self, response):
        self.update()
        decrypted_pack = self.decode(response["pack"])
        self.cipher.verify(base64.b64decode(response["tag"]))
        return decrypted_pack

    def set_key(self, key):
        self.key = key
