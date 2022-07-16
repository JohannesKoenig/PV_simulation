import time
from datetime import datetime
from typing import List
from src.output.cli_output_manager import CLIOutputManager
from src.output.output_manager import OutputManager
from src.generator.power_generator import PowerGenerator
from src.generator.perlin_noise_power_generator import PerlinNoisePowerGenerator

def main():
    print("Starting meter service ...")
    power_generator: PowerGenerator = PerlinNoisePowerGenerator()
    outputs: List[OutputManager] = [CLIOutputManager]
    while(True):
        now = datetime.now()
        value = power_generator.get_value(now.timestamp())
        
        for output in outputs:
            output.process(value, now)

        time.sleep(1)


if __name__ == "__main__":
    main()
