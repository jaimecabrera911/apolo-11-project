from typing import List

from src.models.state import State

'''
Este módulo define la clase Device, que representa un dispositivo espacial con un código único, un nombre y estados
asociados.

Clases:
    - Device: Representa un dispositivo espacial con atributos código, nombre y estados.

Métodos:
    - __init__: Inicializa una instancia de Dispositivo con el código, nombre y estados opcionales proporcionados.
    - to_dict: Convierte la instancia de dispositivo en un diccionario para facilitar la serialización.

Utilización:
    Para utilizar este módulo, importa la clase Device. Cree instancias Device con los parámetros requeridos,
    y utiliza el método to_dict para la serialización.
'''


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
