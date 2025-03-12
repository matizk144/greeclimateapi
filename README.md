## Another GREE HVAC API
The idea of API was written as answer for unstable integration in official plugin in Home Assistant. API is written in Python 3.6+ and exposed as package in pypi called _greeclimateapi_.

## How to use

# Imports
```
from greeclimateapi.greeClimateApi import GreeClimateApi
from greeclimateapi.enums import *
```

# Connect to device
```
device = GreeClimateApi("10.0.4.106", EncryptionType.aes_ecb)
```
At this point API support two encryption modes:
- Legacy: _EncryptionType.aes_ecb_ which is used in WIFI module v1.X
- Newer: _EncryptionType.aes_gcm_ which is used in newer WIFI module above 1.21 (could be lower or above)
If you don't know which encryption to use, try both :)

# Initialization
```
await device.initialize()
```
API try to connect to device and exchange keys. On this point, if connection fails, seams that you have set invalid __EncryptionType_

# Get device status
```
await device.sync_status()
```
API get all parameters from HVAC and cache them

# Available commands to set HVAC
```
await device.power(True)
#await device.target_temperature(21)
#await device.operation_mode(OperationMode.fan)
#await device.fan_speed(FanSpeed.low)
#await device.health(True)
#await device.light(True)
#await device.vertical_swing(VerticalSwing.bottom)
#await device.horizontal_swing(HorizontalSwing.right)
#await device.quiet(False)
```

# Example how to get data
```
await device.sync_status()
temperature = device.statusData.currentTemperature
```
Please keep in mind, that you have to call _sync_status()_ method to get all parameters, before you read someting from _statusData_

# Available parameters to get
```
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
```

