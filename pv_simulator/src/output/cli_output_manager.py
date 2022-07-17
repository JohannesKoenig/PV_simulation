from datetime import datetime
from src.output.output_manager import OutputManager
from src.utils.pv_datapoint import PVDatapoint

class CLIOutputManager(OutputManager):

    def process(self, datapoint: PVDatapoint) -> None:
        print(f'{datapoint.time.strftime("%m/%d/%Y, %H:%M:%S")}: {datapoint.power_value}, {datapoint.pv_power_value}')