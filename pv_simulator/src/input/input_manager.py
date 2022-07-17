from abc import ABC, abstractmethod
from src.utils.datapoint import Datapoint
from typing import Callable

class InputManager(ABC):

    @abstractmethod
    def on_datapoint_input(self, callback: Callable[[Datapoint],None])-> None:
        """
        pass a callback function that should be called, when a new datapoint is received
        """
        pass

    @abstractmethod
    def start(self)-> None:
        """
        start listening
        """
        pass

    
