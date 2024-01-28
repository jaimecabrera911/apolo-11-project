import datetime
from datetime import datetime
from typing import List

from src.models.device import Device

'''
Este módulo define la clase Mission, que representa una misión espacial con un código único, nombre, fecha y dispositivos asociados.

Clases:
    - Mission: Representa una misión espacial con atributos código, nombre, fecha y dispositivos.

Métodos:
    - __init__: Inicializa una instancia de Misión con el código, nombre y dispositivos opcionales proporcionados.
    - to_dict: Convierte la instancia de Misión en un diccionario para facilitar su serialización.

Utilización:
    Para utilizar este módulo, importa la clase Mission. Cree instancias Mission con los parámetros requeridos
    y utilice el método to_dict para la serialización.
'''

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
