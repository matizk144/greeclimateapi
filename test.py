from greeclimateapi.greeClimateApi import GreeClimateApi

import asyncio


async def main():
    device = GreeClimateApi("10.0.4.104")
    await device.initialize()
    await device.sync_status()
    print("Power: " + str(device.statusData.power))


# status = device.sync_status()
# device.power(False)

asyncio.run(main())

print("Dziala")
