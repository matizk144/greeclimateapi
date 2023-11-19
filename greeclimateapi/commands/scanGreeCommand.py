from greeclimateapi.commands.greeCommand import greeCommand


class scanGreeCommand(greeCommand):
    def __init__(self, connection, cipher, factory):
        super().__init__(connection, cipher, factory)

    async def send_command(self):
        scan_request = '{"t": "scan"}'
        scan_response = await self.connection.send_data(scan_request)
        decrypted_pack = self.cipher.decode(scan_response["pack"])
        self.factory.set_mac(decrypted_pack["mac"])
        return self
