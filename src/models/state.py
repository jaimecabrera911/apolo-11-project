'''
Este módulo define la clase State, que representa el estado de un dispositivo espacial con un código y un nombre únicos.

Clases:
    - State: Representa el estado de un dispositivo espacial con atributos código y nombre.

Métodos:
    - __init__: Inicializa una instancia de State con el código y nombre proporcionados.

Utilización:
    Para utilizar este módulo, importa la clase State. Crea instancias de State con los parámetros requeridos.
'''


class State:

    def __init__(self, code: int, name: str) -> None:
        self.code = code
        self.name = name
