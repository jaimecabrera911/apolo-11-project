from typing import List

from src.models.mission import Mission

'''
Este módulo define la clase Project, que representa un proyecto con un código único, un nombre y misiones asociadas.

Clases:
    - Project: Representa un proyecto con atributos código, nombre y misiones.

Métodos:
    - __init__: Inicializa una instancia de Proyecto con el código, nombre y misiones proporcionados.

Utilización:
    Para utilizar este módulo, importa la clase Project. Crea instancias de Proyecto con los parámetros requeridos.
'''

class Project:
    def __init__(self, code: str, name: str, missions: List[Mission]):
        self.code = code
        self.name = name
        self.missions = missions
