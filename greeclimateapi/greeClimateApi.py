from commands.factory import greeCommandFactory
from commands.statusGreeCommand import statusGreeCommand
from greeStatusData import GreeStatusData
from enums import *


class GreeClimateApi:
    def __init__(self, device_ip):
        self.statusData: GreeStatusData
        self.statusCommand: statusGreeCommand
        self.mac = None
        self.commandFactory = greeCommandFactory(device_ip)

    def initialize(self):
        self.commandFactory.create_scan_command().send_command()
        self.commandFactory.create_bind_command().send_command()
        self.statusCommand = self.commandFactory.create_status_command()
        self.status()

    def status(self):
        self.statusCommand.send_command()
        self.statusData = self.statusCommand.statusData

    def power(self, power_state: bool):
        self.commandFactory.create_power_set_command(power_state).send_command()
        self.statusData.power = power_state

    def target_temperature(self, target_temperature: int):
        self.commandFactory.create_target_temperature_set_command(target_temperature).send_command()
        self.statusData.target_temperature = target_temperature

    def operation_mode(self, operation_mode: OperationMode):
        self.commandFactory.create_operation_mode_set_command(operation_mode).send_command()
        self.statusData.operation_mode = operation_mode

    def fan_speed(self, fan_speed: FanSpeed):
        self.commandFactory.create_fan_speed_set_command(fan_speed).send_command()
        self.statusData.fan_speed = fan_speed

    def fresh_air(self, fresh_air: bool):
        self.commandFactory.create_fresh_air_set_command(fresh_air).send_command()
        self.statusData.fresh_air = fresh_air

    def x_fan(self, x_fan: bool):
        self.commandFactory.create_x_fan_set_command(x_fan).send_command()
        self.statusData.x_fan = x_fan

    def health(self, health: bool):
        self.commandFactory.create_health_set_command(health).send_command()
        self.statusData.health = health

    def sleep_mode(self, sleep_mode: bool):
        self.commandFactory.create_sleep_mode_set_command(sleep_mode).send_command()
        self.statusData.sleep_mode = sleep_mode

    def light(self, light: bool):
        self.commandFactory.create_light_set_command(light).send_command()
        self.statusData.light = light

    def horizontal_swing(self, horizontal_swing: HorizontalSwing):
        self.commandFactory.create_horizontal_swing_set_command(horizontal_swing).send_command()
        self.statusData.horizontal_swing = horizontal_swing

    def vertical_swing(self, vertical_swing: VerticalSwing):
        self.commandFactory.create_vertical_swing_set_command(vertical_swing).send_command()
        self.statusData.vertical_swing = vertical_swing

    def quiet(self, quiet: bool):
        self.commandFactory.create_quiet_set_command(quiet).send_command()
        self.statusData.quiet = quiet

    def fan_max(self, fan_max: bool):
        self.commandFactory.create_fan_max_set_command(fan_max).send_command()
        self.statusData.fan_max = fan_max

    def freeze_protection(self, freeze_protection: bool):
        self.commandFactory.create_freeze_protection_set_command(freeze_protection)
        self.statusData.freeze_protection = freeze_protection

    def temperature_unit(self, temperature_unit: TemperatureUnit):
        self.commandFactory.create_temperature_unit_set_command(temperature_unit).send_command()
        self.statusData.temperature_unit = temperature_unit

    def energy_saving(self, energy_saving: bool):
        self.commandFactory.create_energy_saving_set_command(energy_saving).send_command()
        self.statusData.energy_saving = energy_saving

