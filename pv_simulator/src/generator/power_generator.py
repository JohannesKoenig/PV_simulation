from abc import ABC, abstractmethod

class PowerGenerator(ABC):

    @abstractmethod
    def get_value(time: float) -> float:
        """
        Generate a power consumption value sampled at position 'time' from a continuous function.
        """
        pass
