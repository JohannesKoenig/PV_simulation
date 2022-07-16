from abc import ABC, abstractmethod

class OutputManager(ABC):

    @abstractmethod
    def process(power_value: float, timestamp: float) -> None:
        """
        Process the given touple of power_value and timestamp to a specific destination.
        """
        pass
