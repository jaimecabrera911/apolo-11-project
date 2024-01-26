import datetime
import json
import os
import shutil

from ..models.report2 import Report2


class GenerateReport:

    @staticmethod
    def get_data_files() -> list[Report2]:
        directorio = 'devices'
        # Obtener la lista de archivos en el directorio
        archivos_en_directorio = os.listdir(directorio)
        reports: list[Report2] = []

        for nombre_archivo in archivos_en_directorio:
            # Verificar si el nombre del archivo termina en ".json"
            if nombre_archivo.endswith(".json"):
                ruta_completa = os.path.join(directorio, nombre_archivo)

                # Verificar si es un archivo (no es un directorio)
                if os.path.isfile(ruta_completa):
                    # Aquí puedes realizar operaciones con cada archivo
                    with open(ruta_completa, 'r') as archivo:
                        data_json = json.load(archivo)
                    personas: list[Report2] = [Report2(**data) for data in data_json]

                    reports += personas

        return reports

    @staticmethod
    def create_files(report: str, data):
        date_format = datetime.datetime.now().strftime('%d%m%Y%M%S')
        with open(f"devices/APLSTATS-{report}-{date_format}.log", "w") as outfile:
            outfile.write(data)

    def analyze_events(self):
        statistics = {}
        data = self.get_data_files()
        for event in data:
            mission = event.mission
            device = event.device
            state = event.state

            # Crear claves si no existen en el diccionario
            if mission not in statistics:
                statistics[mission] = {}
            if device not in statistics[mission]:
                statistics[mission][device] = {}

            # Contar la cantidad de eventos por estado
            if state not in statistics[mission][device]:
                statistics[mission][device][state] = 1
            else:
                statistics[mission][device][state] += 1

        text = ""
        # Imprimir las estadísticas
        for mission, devices in statistics.items():
            text += f"{mission}\n"
            for device, states in devices.items():
                text += f"  {device}\n"
                for state, count in states.items():
                    text += f"      Estado {state}: {count} eventos\n"

        self.create_files("ANALIZE_DATA", text)

    def manage_disconnections(self):
        # Inicializar un diccionario para realizar un seguimiento de las desconexiones por misión y dispositivo
        disconnections = {}

        data = self.get_data_files()

        text = ""
        # Iterar sobre los datos y contar la cantidad de desconexiones por misión y dispositivo
        for event in data:
            mission = event.mission
            device = event.device
            state = event.state

            # Verificar si el estado es "unknown" y contar la desconexión
            if state == "unknown":
                if mission not in disconnections:
                    disconnections[mission] = {}
                if device not in disconnections[mission]:
                    disconnections[mission][device] = 1
                else:
                    disconnections[mission][device] += 1

        # Imprimir las desconexiones por misión y dispositivo
        for mission, devices in disconnections.items():
            text += f"Misión: {mission}\n"
            for device, count in devices.items():
                text += f"  Dispositivo: {device}, Desconexiones: {count}\n"

        self.create_files("MANAGE_DISCONNECTIONS", text)

    def get_inoperable_devices(self):
        inoperable_devices = set()

        data = self.get_data_files()

        text = ""

        # Iterar sobre los datos y agregar dispositivos inoperables al conjunto
        for event in data:
            state = event.state
            if state in ["unknown", "killed"]:
                inoperable_devices.add(event.device)

        # Imprimir la cantidad y los nombres de dispositivos inoperables
        text += f"Total de dispositivos inoperables: {len(inoperable_devices)}\n"
        text += f"Dispositivos inoperables: {', '.join(inoperable_devices)}\n"
        self.create_files("INOPERABLE_DEVICES", text)

    def calculate_data_percentages(self):
        percentages = {}

        data = self.get_data_files()

        text = ""
        # Iterar sobre los datos y calcular los porcentajes para cada dispositivo y misión
        for event in data:
            mission = event.mission
            device = event.device

            if mission not in percentages:
                percentages[mission] = {}
            if device not in percentages[mission]:
                percentages[mission][device] = 0

            percentages[mission][device] += 1

        # Calcular los porcentajes
        for mission, devices in percentages.items():
            text += f"Misión: {mission}\n"
            for device, count in devices.items():
                total_data = len(data)
                percentage = (count / total_data) * 100
                text += f"Dispositivo: {device}, Porcentaje: {percentage:.2f}%\n"
        self.create_files("CALCULATE_DATA_PERCENTAGES", text)

    @staticmethod
    def create_backup():

        # Ruta del directorio de respaldo
        directorio_respaldo = os.path.join("../devices", '../backup')

        # Obtener la lista de archivos en el directorio actual
        archivos_en_directorio = os.listdir("devices")

        # Filtrar los archivos que terminan en ".log"
        archivos_log = [archivo for archivo in archivos_en_directorio if archivo.endswith('.log')]

        # Mover los archivos al directorio de respaldo
        for archivo in archivos_log:
            ruta_origen = os.path.join("devices/", archivo)
            ruta_destino = os.path.join("backup/", archivo)
            shutil.move(ruta_origen, ruta_destino)
