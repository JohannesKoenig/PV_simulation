from select import select
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
        
        
    def on_datapoint_input(self, callback: Callable[[Datapoint],None])-> None:
        self.callback = callback
        
    
    def start(self)-> None:
        if self.connection == None:
            try:
                print(f"Attempting to connect to {self.host}:{self.port}")
                credentials = PlainCredentials(self.user, self.password)
                self.connection = BlockingConnection(ConnectionParameters(self.host, self.port, credentials=credentials))
                self.channel = self.connection.channel()
                self.channel.queue_declare(self.routing_key)
            except AMQPConnectionError as e:
                print(f"Failed connection to RabbitMQ, {self.host}:{self.port}")
                print(e)
                return
        
        def rabbit_mq_callback(ch, method, properties, body):
            print(f"Received {body}")
            if self.callback != None:
                print("callback should be triggered")
        
        print(self.connection)
        self.channel.basic_consume(queue=self.routing_key, auto_ack=True, on_message_callback=rabbit_mq_callback)
        print(f"Waiting for messages for queue {self.routing_key}...")
        self.channel.start_consuming()