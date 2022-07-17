from dataclasses import dataclass
from datetime import datetime

@dataclass
class PVDatapoint():
    power_value: float
    time: datetime
    pv_power_value: float