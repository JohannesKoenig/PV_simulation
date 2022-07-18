from queue import Queue
from socket import socket
from threading import Thread
import time
from unittest.util import strclass
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
    connection: BlockingConnection
    channel: BlockingChannel
    consumer_thread: Thread
    datapoints: "Queue[Datapoint]"


    def __init__(self, host:str = "localhost", port:int = 5672, routing_key:str = "power_consumption", user: str = "guest", password: str = "password") -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.routing_key = routing_key
        self.datapoints = Queue()
        self.connection = None
        self.channel = None
        self.consumer_thread = Thread(target=self.__execution)
        self.consumer_thread.start()
       
    def process(self, datapoint: Datapoint) -> None:
        self.datapoints.put(datapoint)

    def __execution(self) -> None:
        while(True):
            try:
                if self.channel == None or self.channel.is_closed:
                    self.__connect_to_broker()
                while not self.datapoints.empty():
                    datapoint = self.datapoints.get()
                    self.channel.basic_publish(exchange="",routing_key=self.routing_key, body=datapoint.to_json())
                    print(f"Published datapoint {datapoint.time}, {datapoint.power_value}")
            except AMQPConnectionError:
                print(f"Failed connection to RabbitMQ, {self.host}:{self.port}")
            except Exception as e:
                print(e)
            time.sleep(1)

    def __connect_to_broker(self) -> None:
        credentials = PlainCredentials(self.user, self.password)
        self.connection = BlockingConnection(ConnectionParameters(self.host, self.port, credentials=credentials))    
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.routing_key)
