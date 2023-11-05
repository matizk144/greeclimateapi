from enums import *


class GreeStatusData:
    def __init__(self):
        self.fanMax: bool
        self.quiet: bool
        self.verticalSwing: VerticalSwing
        self.light: bool
        self.horizontalSwing: HorizontalSwing
        self.sleepMode: bool
        self.freezeProtection: bool
        self.energySaving: bool
        self.currentTemperature: int
        self.health: bool
        self.xFan: bool
        self.freshAir: bool
        self.temperatureUnit: TemperatureUnit
        self.fanSpeed: FanSpeed
        self.targetTemperature: int
        self.operationMode: OperationMode
        self.power: bool
