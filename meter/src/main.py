import time
import os
from datetime import datetime
from typing import List
from dotenv import load_dotenv
from src.output.cli_output_manager import CLIOutputManager
from src.output.rabbitmq_output_manager import RabbitMQOutputManager
from src.output.output_manager import OutputManager
from src.generator.power_generator import PowerGenerator
from src.generator.perlin_noise_power_generator import PerlinNoisePowerGenerator
from src.utils.datapoint import Datapoint

def main():
    print("Starting meter service ...")
    load_dotenv()
    RABBIT_MQ_HOST = os.environ.get("RABBIT_MQ_HOSTNAME")
    RABBIT_MQ_PORT = os.environ.get("RABBIT_MQ_PORT")
    RABBIT_MQ_KEY_WORD = os.environ.get("RABBIT_MQ_KEY_WORD")
    RABBIT_MQ_USER = os.environ.get("RABBIT_MQ_USER")
    RABBIT_MQ_PASSWORD = os.environ.get("RABBIT_MQ_PASSWORD")

    power_generator: PowerGenerator = PerlinNoisePowerGenerator()
    outputs: List[OutputManager] = [CLIOutputManager(), RabbitMQOutputManager(RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_KEY_WORD, RABBIT_MQ_USER, RABBIT_MQ_PASSWORD)]
    while(True):
        now = datetime.now()
        value = power_generator.get_value(now.timestamp())
        datapoint = Datapoint(value, now)
        for output in outputs:
            output.process(datapoint)

        time.sleep(1)


if __name__ == "__main__":

    main()
