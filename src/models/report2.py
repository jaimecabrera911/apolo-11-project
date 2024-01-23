from dataclasses import dataclass
from datetime import datetime


@dataclass
class Report2:
    def __init__(self, date: str,device: str, hash: str, mission: str, state: str):
        self.date = date
        self.mission = mission
        self.device = device
        self.state = state
        self.hash = hash

    def to_dict(self):
        return {
            'date': self.date,
            'mission': self.mission,
            'device': self.device,
            'state': self.state,
            'hash': self.hash
        }
