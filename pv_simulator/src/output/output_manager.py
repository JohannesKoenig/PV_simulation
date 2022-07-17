from abc import ABC, abstractmethod
from src.utils.pv_datapoint import PVDatapoint

class OutputManager(ABC):

    @abstractmethod
    def process(self, datapoint: PVDatapoint) -> None:
        """
        Process the given touple of power_value and timestamp to a specific destination.
        """
        pass
