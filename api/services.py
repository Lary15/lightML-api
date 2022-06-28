import time

import model
from model.peripherals_report import PeripheralsReport
from repository.repository import AbstractRepository

def save_report(report: PeripheralsReport, repo: AbstractRepository):
    report.timestamp = int(time.time())
    repo.add(report)