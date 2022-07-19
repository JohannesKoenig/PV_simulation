import unittest
from datetime import datetime
from src.generator.perlin_noise_power_generator import PerlinNoisePowerGenerator

class TestPerlinNoisePowerGenerator(unittest.TestCase):

    def test_times(self):
        generator = PerlinNoisePowerGenerator(0,1000)
     
        def timestamp_by_hour(time: float) -> datetime:
            hour = int(time)
            minute =int((time - hour) * 60)
            dt = datetime.now()
            dt = dt.replace(hour=hour, minute=minute)
            return dt

        for i in range(0,24):
            for j in range(0,60):
                dt = timestamp_by_hour(i + j/60)
                value = generator.get_value(dt.timestamp())
                self.assertTrue(value >= 0 and value <= 1000)
        
