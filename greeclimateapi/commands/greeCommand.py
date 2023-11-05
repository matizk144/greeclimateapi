from abc import ABC, abstractmethod


class greeCommand(ABC):
    def __init__(self, connection, cipher, factory):
        self.connection = connection
        self.cipher = cipher
        self.factory = factory

    @abstractmethod
    def send_command(self):
        pass


class greeSetCommand(ABC):
    def __init__(self, factory):
        self.targetValues = None
        self.parameters = None
        self.factory = factory

    def send_command(self):
        pack_request = {
            "opt": self.parameters,
            "p": self.targetValues,
            "t": "cmd"
        }
        request = {
            "cid": "app",
            "i": 0,
            "pack": self.factory.cipher.encode(str(pack_request).replace("'", '"')),
            "t": "pack",
            "tcid": self.factory.mac,
            "uid": 0
        }
        request_str = str(request).replace("'", '"')
        response = self.factory.connection.send_data(request_str)
        decrypted_pack = self.factory.cipher.decode(response["pack"])
        if decrypted_pack["r"] != 200:
            raise Exception("Set command not finished correctly")
