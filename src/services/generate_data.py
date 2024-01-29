import json
import random
import time
from typing import List

from src.config.config import FILES_QTY, TIME
from src.data.data import get_data
from src.models.mission import Mission
from src.models.report import Report

'''
Este módulo define la clase GenerateData, responsable de generar archivos de datos con reportes aleatorios para misiones
y dispositivos.

Clases:
    - GenerateData: Contiene métodos para ejecutar el proceso de generación de datos.

Métodos:
    - execute: Ejecuta el proceso de generación de datos para un número especificado de ficheros e intervalos de tiempo.
    - generate_data: Genera datos para una misión específica y los escribe en un archivo JSON.

Utilización:
    Para utilizar este módulo, importa la clase GenerateData y llama al método execute para iniciar la generación de
    datos.
'''


class GenerateData:

    @staticmethod
    def execute():
        counter = 1
        size = FILES_QTY + 1
        while counter <= size:
            GenerateData.generate_data(counter)
            time.sleep(TIME)
            counter += 1
            if counter == size:
                counter = 1

    @staticmethod
    def generate_data(counter):
        missions: List[Mission] = get_data()
        number_format = f"{counter:04}"
        for mission in missions:
            data = []
            for device in mission.devices:
                state_random = random.randint(0, len(device.states) - 1)
                report = Report(mission.name, device.name, device.states[state_random].name)
                data.append(report.__dict__)
            name_file = f"APL-{mission.code}-{number_format}.json"

            with open(f"devices/{name_file}", "w") as archivo:
                archivo.write(f"{json.dumps(data)}")
