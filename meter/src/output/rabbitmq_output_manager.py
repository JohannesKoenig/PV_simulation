import dataclasses
import json
from importlib_metadata import os
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
from pika.exceptions import AMQPConnectionError
from src.output.output_manager import OutputManager
from src.utils.datapoint import Datapoint


class RabbitMQOutputManager(OutputManager):

    host: str
    port: int
    routing_key: str

    def __init__(self, host:str = "localhost", port:int = 5672, routing_key:str = "power_consumption") -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.routing_key = routing_key


    def process(self, datapoint: Datapoint) -> None:
        try:
            connection = BlockingConnection(ConnectionParameters(self.host, self.port))
            channel = connection.channel()
            channel.queue_declare(self.routing_key)
            channel.basic_publish(exchange="",routing_key=self.routing_key, body=json.dumps(dataclasses.asdict(datapoint)))
            connection.close()
        except AMQPConnectionError:
            print(f"Failed connection to RabbitMQ, {self.host}:{self.port}")