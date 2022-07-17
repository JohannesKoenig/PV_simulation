from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from datetime import datetime

def time_to_string(time: datetime)-> str:
        return time.isoformat()

@dataclass_json
@dataclass
class Datapoint():
    power_value: float
    time: datetime = field(
        metadata=config(
            encoder=time_to_string
        ))

