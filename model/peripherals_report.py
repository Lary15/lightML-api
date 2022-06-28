from dataclasses import dataclass

@dataclass
class PeripheralsReport:
    """Class for keeping track of all peripherals states (sensors and LED's)"""
    pir: int = 0
    ldr_1: int = 0
    ldr_2: int = 0
    temp: float = 0.0
    mic: float = 0.0
    led_on: bool = False
    led_color: str = "unknown"
    timestamp: int = 0
