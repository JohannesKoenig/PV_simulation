import json
from select import select
from threading import Thread
import time
from dateutil import parser
from typing import Callable
from src.input.input_manager import InputManager
from src.utils.datapoint import Datapoint
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
from pika.credentials import PlainCredentials
from pika.exceptions import AMQPConnectionError

class RabbitMQInputManager(InputManager):

    host: str
    port: int
    user: str
    password: str
    routing_key: str
    callback: Callable[[Datapoint],None]
    connection: BlockingConnection
    channel: BlockingChannel

    def __init__(self, host:str = "localhost", port:int = 5672, routing_key:str = "power_consumption", user: str = "guest", password: str = "password") -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.routing_key = routing_key
        self.connection = None
        self.channel = None
        self.callback = None

        self.consumer_thread = Thread(target=self.__execution)
        self.consumer_thread.start()
        
        
    def on_datapoint_input(self, callback: Callable[[Datapoint],None])-> None:
        self.callback = callback
        
    def __execution(self) -> None:

        def rabbit_mq_callback(ch, method, properties, body):
            decoded = body.decode()
            if self.callback != None:
                body_dict = json.loads(decoded)
                datapoint = Datapoint(time=parser.parse(body_dict["time"]), power_value=body_dict["power_value"])
                self.callback(datapoint)


        while(True):
            try:
                if self.channel == None or self.channel.is_closed:
                    self.__connect_to_broker()
                    print("Established connection")
                    self.channel.basic_consume(queue=self.routing_key, auto_ack=True, on_message_callback=rabbit_mq_callback)
                    print(f"Waiting for messages for queue {self.routing_key}...")
                    self.channel.start_consuming()

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