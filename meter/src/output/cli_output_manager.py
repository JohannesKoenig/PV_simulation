from datetime import datetime
from src.output.output_manager import OutputManager
from src.utils.datapoint import Datapoint

class CLIOutputManager(OutputManager):

    def process(self, datapoint: Datapoint) -> None:
        print(f'{datapoint.time.strftime("%m/%d/%Y, %H:%M:%S")}: {datapoint.power_value}')