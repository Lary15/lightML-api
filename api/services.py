from builtins import breakpoint
import time
import os
import requests
from typing import Tuple

from model.peripherals_report import PeripheralsReport
from repository.repository import AbstractRepository

def save_report(report: PeripheralsReport, repo: AbstractRepository):
    # insert lamp info
    report.led_on, report.led_color, report.led_dimmer = query_lamp_details()
    # insert timestamp info
    report.timestamp = int(time.time())
    repo.add(report)

def query_lamp_details() -> Tuple[int, str, int]:
    try:
        response = requests.get(f"{os.getenv('LAMP_URL')}/cm?cmnd=HsbColor", timeout=1).json()
        return int(response["POWER"] == "ON"), response["Color"], response["Dimmer"]
    except requests.exceptions.ConnectionError:
        return 0, "0000000000", 0