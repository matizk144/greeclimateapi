from commands.greeCommand import greeSetCommand


class powerGreeSetCommand(greeSetCommand):
    def __init__(self, factory, power_state):
        super().__init__(factory)
        self.parameters = ["Pow"]
        self.targetValues = [int(power_state)]


class targetTemperatureGreeSetCommand(greeSetCommand):
    def __init__(self, factory, target_temperature):
        super().__init__(factory)
        self.parameters = ["TempUn", "SetTem"]
        self.targetValues = [0, int(target_temperature)]


class operationModeGreeSetCommand(greeSetCommand):
    def __init__(self, factory, operation_mode):
        super().__init__(factory)
        self.parameters = ["Mod"]
        self.targetValues = [operation_mode.value]


class fanSpeedGreeSetCommand(greeSetCommand):
    def __init__(self, factory, fan_speed):
        super().__init__(factory)
        self.parameters = ["WdSpd"]
        self.targetValues = [fan_speed.value]


class freshAirGreeSetCommand(greeSetCommand):
    def __init__(self, factory, fresh_air):
        super().__init__(factory)
        self.parameters = ["Air"]
        self.targetValues = [int(fresh_air)]


class xFanGreeSetCommand(greeSetCommand):
    def __init__(self, factory, x_fan):
        super().__init__(factory)
        self.parameters = ["Blo"]
        self.targetValues = [int(x_fan)]


class healthGreeSetCommand(greeSetCommand):
    def __init__(self, factory, health):
        super().__init__(factory)
        self.parameters = ["Health"]
        self.targetValues = [int(health)]


class sleepModeGreeSetCommand(greeSetCommand):
    def __init__(self, factory, sleep_mode):
        super().__init__(factory)
        self.parameters = ["SwhSlp"]
        self.targetValues = [int(sleep_mode)]


class lightGreeSetCommand(greeSetCommand):
    def __init__(self, factory, light):
        super().__init__(factory)
        self.parameters = ["Lig"]
        self.targetValues = [int(light)]


class horizontalSwingGreeSetCommand(greeSetCommand):
    def __init__(self, factory, horizontal_swing):
        super().__init__(factory)
        self.parameters = ["SwingLfRig"]
        self.targetValues = [horizontal_swing.value]


class verticalSwingGreeSetCommand(greeSetCommand):
    def __init__(self, factory, vertical_swing):
        super().__init__(factory)
        self.parameters = ["SwUpDn"]
        self.targetValues = [vertical_swing.value]


class quietGreeSetCommand(greeSetCommand):
    def __init__(self, factory, quiet):
        super().__init__(factory)
        self.parameters = ["Quiet"]
        self.targetValues = [int(quiet)]


class fanMaxGreeSetCommand(greeSetCommand):
    def __init__(self, factory, fan_max):
        super().__init__(factory)
        self.parameters = ["Tur"]
        self.targetValues = [int(fan_max)]


class freezeProtectionGreeSetCommand(greeSetCommand):
    def __init__(self, factory, freeze_protection):
        super().__init__(factory)
        self.parameters = ["StHt"]
        self.targetValues = [int(freeze_protection)]


class temperatureUnitGreeSetCommand(greeSetCommand):
    def __init__(self, factory, temperature_unit):
        super().__init__(factory)
        self.parameters = ["TemUn"]
        self.targetValues = [temperature_unit.value]


class energySavingGreeSetCommand(greeSetCommand):
    def __init__(self, factory, energy_saving):
        super().__init__(factory)
        self.parameters = ["SvSt"]
        self.targetValues = [int(energy_saving)]