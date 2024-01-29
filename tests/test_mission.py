from src.models.mission import Mission
from src.models.device import Device

def test_mission_initialization():
    # Prueba la inicialización de una misión sin dispositivos
    mission = Mission(code="ORBONE", name="OrbitOne")
    assert mission.code == "ORBONE"
    assert mission.name == "OrbitOne"
    assert mission.date is not None  # Verifica que la fecha no sea nula
    assert mission.devices == []

def test_mission_with_devices():
    # Prueba la inicialización de una misión con dispositivos
    devices = [Device(code=1, name="Satelite"), Device(code=2, name="Nave")]
    mission = Mission(code="CLNM", name="ColonyMoon", devices=devices)
    assert mission.code == "CLNM"
    assert mission.name == "ColonyMoon"
    assert mission.date is not None
    assert mission.devices == devices

def test_mission_to_dict():
    # Prueba la conversión a un diccionario
    devices = [Device(code=1, name="Satelite"), Device(code=2, name="Nave")]
    mission = Mission(code="TMRS", name="VacMars", devices=devices)
    expected_dict = {
        'code': 'TMRS',
        'name': 'VacMars',
        'date': mission.date.isoformat(),
        'devices': [
            {'code': 1, 'name': 'Satelite', 'states': []},
            {'code': 2, 'name': 'Nave', 'states': []}
        ]
    }
    assert mission.to_dict() == expected_dict
