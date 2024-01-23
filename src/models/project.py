from typing import List

from src.models.mission import Mission


class Project:
    def __init__(self, code: str, name: str, missions: List[Mission]):
        self.code = code
        self.name = name
        self.missions = missions
