from src.output.file_output_manager import FileOutputManager
import unittest
import os
from datetime import datetime
from src.utils.pv_datapoint import PVDatapoint

class TestFileOutputManager(unittest.TestCase):
    
    def test_write(self):
        manager = FileOutputManager("test.dat")
        dt = datetime.now()
        iso_string = dt.isoformat() 
        pv_value = 1
        meter_value = 1
        sum = pv_value + meter_value
        dp = PVDatapoint(meter_value, dt, pv_value)
        manager.process(dp)
        with open("test.dat", "r") as file:
            line = file.readline()
            sub_strings = line.split(',')
            self.assertEqual(sub_strings[0], iso_string)
            self.assertEqual(float(sub_strings[1]), meter_value)
            self.assertEqual(float(sub_strings[2]), pv_value)
            self.assertEqual(float(sub_strings[3]), sum)
        os.remove("test.dat")
