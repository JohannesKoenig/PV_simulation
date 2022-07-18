import os
from typing import List
from dotenv import load_dotenv
from src.output.file_output_manager import FileOutputManager
from src.output.cli_output_manager import CLIOutputManager
from src.output.output_manager import OutputManager
from src.utils.pv_datapoint import PVDatapoint
from src.input.input_manager import InputManager
from src.input.rabbit_mq_input_manager import RabbitMQInputManager
from src.utils.datapoint import Datapoint

def main():
    print("Starting meter service ...")
    load_dotenv()
    RABBIT_MQ_HOST = os.environ.get("RABBIT_MQ_HOSTNAME")
    RABBIT_MQ_PORT = os.environ.get("RABBIT_MQ_PORT")
    RABBIT_MQ_KEY_WORD = os.environ.get("RABBIT_MQ_KEY_WORD")
    RABBIT_MQ_USER = os.environ.get("RABBIT_MQ_USER")
    RABBIT_MQ_PASSWORD = os.environ.get("RABBIT_MQ_PASSWORD")

    input: InputManager = RabbitMQInputManager(RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_KEY_WORD, RABBIT_MQ_USER, RABBIT_MQ_PASSWORD)
    outputs: List[OutputManager] = [CLIOutputManager(), FileOutputManager()]

    def on_datapoint_received(datapoint: Datapoint) -> None:
        # Generate PV value
        # print triple to cli
        # append triple to log file
        pv_value = 1
        pv_datapoint = PVDatapoint(datapoint.power_value, datapoint.time, pv_value)
        for output in outputs:
            output.process(pv_datapoint)
        pass

    input.on_datapoint_input(on_datapoint_received)

if __name__ == "__main__":
    main()
