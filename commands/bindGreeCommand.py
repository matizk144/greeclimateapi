from commands.greeCommand import greeCommand


class bindGreeCommand(greeCommand):
    def __init__(self, connection, cipher, factory):
        super().__init__(connection, cipher, factory)

    def send_command(self):
        pack_request = '{"mac": "' + self.factory.mac + '", "t": "bind", "uid": 0}'
        request = {
            "cid": "app",
            "i": 1,
            "pack": self.cipher.encode(pack_request),
            "t": "pack",
            "tcid": self.factory.mac,
            "uid": 0
        }
        request_str = str(request).replace("'", '"')
        response = self.connection.send_data(request_str)
        decrypted_pack = self.cipher.decode(response["pack"])
        if decrypted_pack["t"] != "bindok":
            raise Exception("Device cannot bind")
        self.factory.set_key(decrypted_pack["key"])