import json

from src.models.device import Device
from src.models.mission import Mission
from src.models.state import State

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
