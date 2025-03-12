from greeclimateapi.greeClimateApi import GreeClimateApi
from greeclimateapi.enums import *

import asyncio


async def main():
#    device = GreeClimateApi("10.0.4.106", EncryptionType.aes_ecb)
    device = GreeClimateApi("10.0.4.108", EncryptionType.aes_gcm)
    await device.initialize()
    await device.sync_status()
    await device.power(False)
    #await device.target_temperature(21)
    #await device.operation_mode(OperationMode.fan)
    #await device.fan_speed(FanSpeed.low)
    #await device.health(True)
    #await device.light(True)
    #await device.vertical_swing(VerticalSwing.bottom)
    #await device.horizontal_swing(HorizontalSwing.right)
    #await device.quiet(False)
    #await device.sleep_mode(False)
    print("Power: " + str(device.statusData.power))


# status = device.sync_status()
# device.power(False)

asyncio.run(main())

print("Dziala")
