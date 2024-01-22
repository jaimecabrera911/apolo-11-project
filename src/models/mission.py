import datetime
from datetime import datetime
from typing import List

from src.models.device import Device


class Mission:

    def __init__(self, code: str, name: str, devices: List[Device] = None) -> None:
        self.code = code
        self.name = name
        self.date = datetime.now()
        self.devices = devices or []

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'date': self.date.isoformat(),
            'devices': [device.to_dict() for device in self.devices]
        }
