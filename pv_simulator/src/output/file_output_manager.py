from datetime import datetime
from src.output.output_manager import OutputManager
from src.utils.pv_datapoint import PVDatapoint

class FileOutputManager(OutputManager):

    file_name: str

    def __init__(self, file_name: str = "log.dat") -> None:
        super().__init__()
        self.file_name = file_name

    def process(self, datapoint: PVDatapoint) -> None:
        with open(self.file_name, "a") as file:
            meter_value = datapoint.power_value
            pv_value = datapoint.pv_power_value
            sum = meter_value + pv_value
            file.write(f"{datapoint.time.isoformat()},{meter_value},{pv_value},{sum}\n")