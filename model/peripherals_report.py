from dataclasses import dataclass

@dataclass
class PeripheralsReport:
    """Class for keeping track of all peripherals states (sensors and LED's)"""
    pir: int
    ldr_1: int
    ldr_2: int
    temp: float
    mic: float
    led_on: bool = False
    led_color: str = "unknown"
    timestamp: int = 0