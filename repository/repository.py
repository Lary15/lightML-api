import abc
from model.peripherals_report import PeripheralsReport

class AbstractRepository(abc.ABC):
  @abc.abstractmethod
  def add(self, model: PeripheralsReport):
    raise NotImplementedError
  
  @abc.abstractmethod
  def get(self, reference) -> dict:
      raise NotImplementedError

  @abc.abstractmethod
  def list(self) -> dict:
      raise NotImplementedError

  @abc.abstractmethod
  def query_by_epoch(self, start: int, end: int) -> dict:
      raise NotImplementedError