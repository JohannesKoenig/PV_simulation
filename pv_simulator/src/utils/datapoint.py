from dataclasses import dataclass
from datetime import datetime

@dataclass
class Datapoint():
    power_value: float
    time: datetime