from greeclimateapi.commands.greeCommand import greeCommand


class bindGreeCommand(greeCommand):
    def __init__(self, connection, cipher, factory):
        super().__init__(connection, cipher, factory)

    async def send_command(self):
        pack_request = '{"mac": "' + self.factory.mac + '", "t": "bind", "uid": 0}'
        request = {
            "cid": "app",
            "i": 1,
            "t": "pack",
            "tcid": self.factory.mac,
            "uid": 0
        }
        request_str = self.cipher.encrypt_pack_parameter(request, pack_request)
        response = await self.connection.send_data(request_str)
        decrypted_pack = self.cipher.decode_pack_parameter(response)
        if decrypted_pack["t"] != "bindok":
            raise Exception("Device cannot bind")
        self.factory.set_key(decrypted_pack["key"])