import unittest
from datetime import datetime
from src.generator.pv_power_generator import PVPowerGenerator

class TestPVPowerGenerator(unittest.TestCase):

    def test_times(self):
        generator = PVPowerGenerator()
        def for_time(time: float, expected: float) -> None:
            self.assertAlmostEqual(generator.get_value(time), expected)

        def timestamp_by_hour(time: float) -> datetime:
            hour = int(time)
            minute = (time - hour) * 60
            dt = datetime.now()
            dt = dt.replace(hour=hour, minute=minute)
            return dt

        dt = timestamp_by_hour(4)
        self.assertAlmostEqual(dt.hour, 4)
        for_time(dt.timestamp(), 0)
        dt = timestamp_by_hour(5)
        for_time(dt.timestamp(), 0)
        dt = timestamp_by_hour(8)
        for_time(dt.timestamp(), 250)
        dt = timestamp_by_hour(14)
        for_time(dt.timestamp(), 3250)
        dt = timestamp_by_hour(20)
        for_time(dt.timestamp(), 100)
        dt = timestamp_by_hour(21)
        for_time(dt.timestamp(), 0)
        dt = timestamp_by_hour(22)
        for_time(dt.timestamp(), 0)
        
