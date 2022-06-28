from flask_restful import Resource
from flask import Response, request
from model.peripherals_report import PeripheralsReport
from repository.repository import AbstractRepository

from api.services import save_report

class Peripherals(Resource):
  def __init__(self, repo: AbstractRepository):
    self.repo = repo

  def post(self) -> Response:
    report = PeripheralsReport(**request.get_json(force=True))
    save_report(report, self.repo)
    return "OK"

  def get(self)  -> Response:
    print(self.repo.list())
    return self.repo.list()