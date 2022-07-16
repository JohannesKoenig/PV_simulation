from datetime import datetime
from src.output.output_manager import OutputManager

class CLIOutputManager(OutputManager):

    def process(power_value: float, time: 'datetime') -> None:
        print(f'{time.strftime("%m/%d/%Y, %H:%M:%S")}: {power_value}')