from datetime import datetime

'''
Este módulo define la clase Report, que representa un reporte con información sobre una misión, un dispositivo,
un estado y una marca de tiempo.

Clases:
    - Report: Representa un reporte con atributos fecha, misión, dispositivo, estado y hash.

Métodos:
    - __init__: Inicializa una instancia de Report con la misión, dispositivo y estado proporcionados.
    - __hash__: Calcula el valor hash de la instancia de reporte basándose en la misión, el dispositivo, el estado
    y la fecha.
    - to_dict: Convierte la instancia de informe en un diccionario para facilitar su serialización.

Utilización:
    Para utilizar este módulo, importe la clase Report. Cree instancias de Report con los parámetros requeridos.
'''


class Report:
    def __init__(self, mission: str, device: str, state: str):
        self.date = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.mission = mission
        self.device = device
        self.state = state
        self.hash = self.__hash__()

    def __hash__(self) -> int:
        if self.mission != "Unknown":
            return hash((self.date, self.mission, self.device, self.state))
        else:
            return 0

    def to_dict(self):
        return {
            'date': self.date,
            'mission': self.mission,
            'device': self.device,
            'state': self.state,
            'hash': self.hash
        }
