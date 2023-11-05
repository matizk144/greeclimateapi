from greeclimateapi.commands.greeCommand import *
from greeclimateapi.greeStatusData import *
from greeclimateapi.enums import *


class statusGreeCommand(greeCommand):
    def __init__(self, connection, cipher, factory):
        super().__init__(connection, cipher, factory)
        self.statusData = GreeStatusData()

    def send_command(self):
        pack_request = {
            "cols": [
                "Pow",
                "Mod",
                "SetTem",
                "WdSpd",
                "Air",
                "Blo",
                "Health",
                "SwhSlp",
                "Lig",
                "SwingLfRig",
                "SwUpDn",
                "Quiet",
                "Tur",
                "StHt",
                "TemUn",
                "HeatCoolType",
                "TemRec",
                "SvSt",
                "TemSen"
            ],
            "mac": "<MAC address>",
            "t": "status"
        }
        request = {
            "cid": "app",
            "i": 0,
            "pack": self.cipher.encode(str(pack_request).replace("'", '"')),
            "t": "pack",
            "tcid": self.factory.mac,
            "uid": 0
        }
        request_str = str(request).replace("'", '"')
        response = self.connection.send_data(request_str)
        decrypted_pack = self.cipher.decode(response["pack"])
        self.statusData = GreeStatusData()
        self.statusData.power = bool(decrypted_pack["dat"][0])
        self.statusData.operationMode = OperationMode(decrypted_pack["dat"][1])
        self.statusData.targetTemperature = int(decrypted_pack["dat"][2])
        self.statusData.fanSpeed = FanSpeed(decrypted_pack["dat"][3])
        self.statusData.freshAir = bool(decrypted_pack["dat"][4])
        self.statusData.xFan = bool(decrypted_pack["dat"][5])
        self.statusData.health = bool(decrypted_pack["dat"][6])
        self.statusData.sleepMode = bool(decrypted_pack["dat"][7])
        self.statusData.light = bool(decrypted_pack["dat"][8])
        self.statusData.horizontalSwing = HorizontalSwing(decrypted_pack["dat"][9])
        self.statusData.verticalSwing = VerticalSwing(decrypted_pack["dat"][10])
        self.statusData.quiet = bool(decrypted_pack["dat"][11])
        self.statusData.fanMax = bool(decrypted_pack["dat"][12])
        self.statusData.freezeProtection = bool(decrypted_pack["dat"][13])
        self.statusData.temperatureUnit = TemperatureUnit(decrypted_pack["dat"][14])
        self.statusData.energySaving = bool(decrypted_pack["dat"][17])
        self.statusData.currentTemperature = int(decrypted_pack["dat"][18]) - 40
