from abc import ABC, abstractmethod
from src.utils.datapoint import Datapoint

class OutputManager(ABC):

    @abstractmethod
    def process(datapoint: Datapoint) -> None:
        """
        Process the given touple of power_value and timestamp to a specific destination.
        """
        pass
