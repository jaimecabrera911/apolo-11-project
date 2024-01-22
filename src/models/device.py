from typing import List

from src.models.state import State


class Device:

    def __init__(self, code: int, name: str, states: List[State] = None) -> None:
        self.code = code
        self.name = name
        self.states = states or []

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'states': [state.__dict__ for state in self.states]
        }