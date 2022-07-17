import dataclasses
import json
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
from pika.exceptions import AMQPConnectionError
from pika.credentials import PlainCredentials
from src.output.output_manager import OutputManager
from src.utils.datapoint import Datapoint


class RabbitMQOutputManager(OutputManager):

    host: str
    port: int
    user: str
    password: str
    routing_key: str

    def __init__(self, host:str = "localhost", port:int = 5672, routing_key:str = "power_consumption", user: str = "guest", password: str = "password") -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.routing_key = routing_key


    def process(self, datapoint: Datapoint) -> None:
        try:
            credentials = PlainCredentials(self.user, self.password)
            connection = BlockingConnection(ConnectionParameters(self.host, self.port, credentials=credentials))    
            channel = connection.channel()
            channel.queue_declare(self.routing_key)
            channel.basic_publish(exchange="",routing_key=self.routing_key, body=datapoint.to_json())
            connection.close()
        except AMQPConnectionError:
            print(f"Failed connection to RabbitMQ, {self.host}:{self.port}")