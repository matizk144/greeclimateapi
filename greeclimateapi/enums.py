from enum import Enum


class FanSpeed(Enum):
    auto = 0
    low = 1
    mediumLow = 2
    medium = 3
    mediumHigh = 4
    high = 5


class OperationMode(Enum):
    auto = 0
    cool = 1
    dry = 2
    fan = 3
    heat = 4


class HorizontalSwing(Enum):
    default = 0
    full = 1
    left = 2
    leftMid = 3
    mid = 4
    rightMid = 5
    right = 6


class VerticalSwing(Enum):
    default = 0
    full = 1
    top = 2
    topMid = 3
    mid = 4
    bottomMid = 5
    bottom = 6
    bottomSwing = 7
    bottomMidSwing = 8
    midSwing = 9
    topMidSwing = 10
    topSwing = 11


class TemperatureUnit(Enum):
    celsius = 0
    fahrenheit = 1