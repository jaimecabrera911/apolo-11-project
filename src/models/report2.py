from dataclasses import dataclass

'''
Este módulo define la clase de datos Report2, que representa un reporte con información sobre fecha, misión,
dispositivo, estado y hash.

Clases de datos:
    - Report2: Representa un informe con atributos fecha, misión, dispositivo, estado y hash.

Métodos:
    - to_dict: Convierte la instancia Report2 en un diccionario para facilitar su serialización.

Utilización:
    Para utilizar este módulo, importa la clase de datos Report2. Crea instancias de Report2 con los parámetros
    requeridos.
'''


@dataclass
class Report2:
    def __init__(self, date: str, device: str, hash: str, mission: str, state: str):
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
