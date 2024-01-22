from typing import List

from src.models.mission import Mission


class Project:
    def __init__(self, code: str, name: str, missions: List[Mission]):
        self.code = code
        self.name = name
        self.missions = missions


''' def generate_file_content(self):
     file_content = f"Fecha: {self.date}\n"
     file_content += f"Misión: {self.mission}\n"
     file_content += f"Tipo de dispositivo: {self.device_type}\n"
     file_content += f"Estado del dispositivo: {self.device_state}\n"
     file_content += f"Hash: {self.__hash__()}\n"
     return file_content

 def __hash__(self) -> int:
     return hash((self.mission, self.device_type, self.date, self.device_state))'''
