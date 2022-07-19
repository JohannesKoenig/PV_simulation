import math
from src.generator.power_generator import PowerGenerator
from datetime import datetime
import numpy as np

class PVPowerGenerator(PowerGenerator):

    linear_morning: np.poly1d
    linear_evening: np.poly1d
    quadratic_day: np.poly1d

    def __init__(self) -> None:
        super().__init__()
        self.linear_morning = np.poly1d(np.polyfit([5, 8], [0, 250], 1))
        self.linear_evening = np.poly1d(np.polyfit([20, 21], [100,0], 1))
        self.quadratic_day = np.poly1d(np.polyfit([8, 14, 20], [250, 3250, 100], 2))

    def get_value(self, time: float) -> float:
        dt = datetime.fromtimestamp(time)
        hour = dt.hour + dt.minute / 60
        if hour > 5 and hour < 8:
            return self.linear_morning(hour)
        elif hour >= 8 and hour <= 20:
            return self.quadratic_day(hour)
        elif hour > 20 and hour < 21:
            return self.linear_evening(hour)
        else:
            return 0
