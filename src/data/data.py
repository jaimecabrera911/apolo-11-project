import json

from ..models.device import Device
from ..models.mission import Mission
from ..models.state import State

'''
Este módulo proporciona funciones para recuperar datos predefinidos relacionados con misiones, dispositivos y estados.
Los datos se almacenan en formato JSON y se utilizan para inicializar instancias de las clases Misión, Dispositivo y Estado.

Clases:
    - Mission: Representa una misión espacial con un código y un nombre únicos.
    - Device: Representa un dispositivo espacial con un código y un nombre únicos.
    - Satet: Representa el estado de un dispositivo espacial con un código y nombre únicos.

Funciones:
    - get_data(): Recupera e inicializa datos predefinidos para misiones, dispositivos y estados.
    
Utilización:
    Para utilizar este módulo, impórtelo y llame a la función get_data(). Devuelve una lista de instancias de misiones
    con los dispositivos y estados asociados.
'''

data_missions = '''
[
  {
    "code": "ORBONE",
    "name": "OrbitOne"
  },
  {
    "code": "CLNM",
    "name": "ColonyMoon"
  },
  {
    "code": "TMRS",
    "name": "VacMars"
  },
  {
    "code": "GALXONE",
    "name": "GalaxyOne"
  },
  {
    "code": "UNKN",
    "name": "Unknown"
  }
]
'''

data_devices = '''
[
  {
    "code": "001",
    "name": "Satelite"
  },
  {
    "code": "002",
    "name": "Nave"
  },
  {
    "code": "003",
    "name": "Traje"
  },
  {
    "code": "004",
    "name": "Vehiculo"
  },
  {
    "code": "005",
    "name": "Robot"
  }
]
'''

data_states = '''
[
    {
      "code":"001",
      "name":"excellent"
    },
     {
      "code":"002",
      "name":"good"
    },
     {
      "code":"003",
      "name":"warning"
    },
     {
      "code":"004",
      "name":"falty"
    },
     {
      "code":"005",
      "name":"killed"
    },
    {
      "code":"006",
      "name":"unknown"
    }
  ]
'''


def get_data():
    states = [State(**state) for state in json.loads(data_states)]
    devices = [Device(**device) for device in json.loads(data_devices)]
    for device in devices:
        device.states = states

    missions = [Mission(**mission) for mission in json.loads(data_missions)]

    for mission in missions:
        mission.devices = devices

    return missions
