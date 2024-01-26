import json
import os
import random
import shutil
import time
from typing import List

from src.config.config import FILES_QTY, TIME
from src.data.data import get_data
from src.models.mission import Mission
from src.models.report import Report


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
