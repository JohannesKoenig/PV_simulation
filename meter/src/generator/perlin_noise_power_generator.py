from datetime import datetime
from src.generator.power_generator import PowerGenerator
from perlin_noise import PerlinNoise


class PerlinNoisePowerGenerator(PowerGenerator):

    min_value: float
    max_value: float
    noise: PerlinNoise

    def __init__(self, min_value:float = 0, max_value:float = 9000, seed:int = 1) -> None:
        super().__init__()
        self.noise = PerlinNoise(seed)
        self.min_value = min_value
        self.max_value = max_value

    def get_value(self, timestamp: float) -> float:
        rnd = self.noise(timestamp)
        normalized = (rnd + 1) / 2
        value = normalized * (self.max_value - self.min_value) + self.min_value
        return value


