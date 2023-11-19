from greeclimateapi.commands.factory import greeCommandFactory
from greeclimateapi.commands.statusGreeCommand import statusGreeCommand
from greeclimateapi.greeStatusData import GreeStatusData
from greeclimateapi.enums import *


class GreeClimateApi:
    def __init__(self, device_ip):
        self.statusData = GreeStatusData()
        self.statusCommand: statusGreeCommand
        self.mac = None
        self.commandFactory = greeCommandFactory(device_ip)

    async def initialize(self):
        await self.commandFactory.create_scan_command().send_command()
        await self.commandFactory.create_bind_command().send_command()
        self.statusCommand = self.commandFactory.create_status_command()

    async def sync_status(self) -> GreeStatusData:
        await self.statusCommand.send_command()
        self.statusData = self.statusCommand.statusData
        return self.statusData

    def status(self) -> GreeStatusData:
        return self.statusData

    async def power(self, power_state: bool):
        await self.commandFactory.create_power_set_command(power_state).send_command()
        self.statusData.power = power_state

    async def target_temperature(self, target_temperature: int):
        await self.commandFactory.create_target_temperature_set_command(target_temperature).send_command()
        self.statusData.target_temperature = target_temperature

    async def operation_mode(self, operation_mode: OperationMode):
        await self.commandFactory.create_operation_mode_set_command(operation_mode).send_command()
        self.statusData.operation_mode = operation_mode

    async def fan_speed(self, fan_speed: FanSpeed):
        await self.commandFactory.create_fan_speed_set_command(fan_speed).send_command()
        self.statusData.fan_speed = fan_speed

    async def fresh_air(self, fresh_air: bool):
        await self.commandFactory.create_fresh_air_set_command(fresh_air).send_command()
        self.statusData.fresh_air = fresh_air

    async def x_fan(self, x_fan: bool):
        await self.commandFactory.create_x_fan_set_command(x_fan).send_command()
        self.statusData.x_fan = x_fan

    async def health(self, health: bool):
        await self.commandFactory.create_health_set_command(health).send_command()
        self.statusData.health = health

    async def sleep_mode(self, sleep_mode: bool):
        await self.commandFactory.create_sleep_mode_set_command(sleep_mode).send_command()
        self.statusData.sleep_mode = sleep_mode

    async def light(self, light: bool):
        await self.commandFactory.create_light_set_command(light).send_command()
        self.statusData.light = light

    async def horizontal_swing(self, horizontal_swing: HorizontalSwing):
        await self.commandFactory.create_horizontal_swing_set_command(horizontal_swing).send_command()
        self.statusData.horizontal_swing = horizontal_swing

    async def vertical_swing(self, vertical_swing: VerticalSwing):
        await self.commandFactory.create_vertical_swing_set_command(vertical_swing).send_command()
        self.statusData.vertical_swing = vertical_swing

    async def quiet(self, quiet: bool):
        await self.commandFactory.create_quiet_set_command(quiet).send_command()
        self.statusData.quiet = quiet

    async def fan_max(self, fan_max: bool):
        await self.commandFactory.create_fan_max_set_command(fan_max).send_command()
        self.statusData.fan_max = fan_max

    async def freeze_protection(self, freeze_protection: bool):
        await self.commandFactory.create_freeze_protection_set_command(freeze_protection)
        self.statusData.freeze_protection = freeze_protection

    async def temperature_unit(self, temperature_unit: TemperatureUnit):
        await self.commandFactory.create_temperature_unit_set_command(temperature_unit).send_command()
        self.statusData.temperature_unit = temperature_unit

    async def energy_saving(self, energy_saving: bool):
        await self.commandFactory.create_energy_saving_set_command(energy_saving).send_command()
        self.statusData.energy_saving = energy_saving

