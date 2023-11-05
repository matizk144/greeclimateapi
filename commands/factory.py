from commands.primitivies import greeDeviceCipher, greeDeviceConnection
from commands.scanGreeCommand import scanGreeCommand
from commands.bindGreeCommand import bindGreeCommand
from commands.statusGreeCommand import statusGreeCommand
from commands.greeSetCommands import *


class greeCommandFactory:
    def __init__(self, device_ip):
        self.connection = greeDeviceConnection(device_ip)
        self.cipher = greeDeviceCipher()
        self.mac = None

    def set_mac(self, mac):
        self.mac = mac

    def set_key(self, key):
        self.cipher.set_key(key)

    def create_scan_command(self):
        return scanGreeCommand(self.connection, self.cipher, self)

    def create_bind_command(self):
        return bindGreeCommand(self.connection, self.cipher, self)

    def create_status_command(self):
        return statusGreeCommand(self.connection, self.cipher, self)

    def create_power_set_command(self, power_state):
        return powerGreeSetCommand(self, power_state)

    def create_target_temperature_set_command(self, target_temperature):
        return targetTemperatureGreeSetCommand(self, target_temperature)

    def create_operation_mode_set_command(self, operation_mode):
        return operationModeGreeSetCommand(self, operation_mode)

    def create_fan_speed_set_command(self, fan_speed):
        return fanSpeedGreeSetCommand(self, fan_speed)

    def create_fresh_air_set_command(self, fresh_air):
        return freshAirGreeSetCommand(self, fresh_air)

    def create_x_fan_set_command(self, x_fan):
        return xFanGreeSetCommand(self, x_fan)

    def create_health_set_command(self, health):
        return healthGreeSetCommand(self, health)

    def create_sleep_mode_set_command(self, sleep_mode):
        return sleepModeGreeSetCommand(self, sleep_mode)

    def create_light_set_command(self, light):
        return lightGreeSetCommand(self, light)

    def create_horizontal_swing_set_command(self, horizontal_swing):
        return horizontalSwingGreeSetCommand(self, horizontal_swing)

    def create_vertical_swing_set_command(self, vertical_swing):
        return verticalSwingGreeSetCommand(self, vertical_swing)

    def create_quiet_set_command(self, quiet):
        return quietGreeSetCommand(self, quiet)

    def create_fan_max_set_command(self, fan_max):
        return fanMaxGreeSetCommand(self, fan_max)

    def create_freeze_protection_set_command(self, freeze_protection):
        return freezeProtectionGreeSetCommand(self, freeze_protection)

    def create_temperature_unit_set_command(self, temperature_unit):
        return temperatureUnitGreeSetCommand(self, temperature_unit)

    def create_energy_saving_set_command(self, energy_saving):
        return energySavingGreeSetCommand(self, energy_saving)