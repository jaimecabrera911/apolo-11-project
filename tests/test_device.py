from src.models.device import Device
from src.models.state import State

def test_device_initialization():
    # Prueba la inicialización de un dispositivo sin estados
    device = Device(code=1, name="Satelite")
    assert device.code == 1
    assert device.name == "Satelite"
    assert device.states == []

def test_device_with_states():
    # Prueba la inicialización de un dispositivo con estados
    states = [State(code=1, name="Good"), State(code=2, name="Bad")]
    device = Device(code=2, name="Nave", states=states)
    assert device.code == 2
    assert device.name == "Nave"
    assert device.states == states

def test_device_to_dict():
    # Prueba la conversión a un diccionario
    states = [State(code=1, name="Good"), State(code=2, name="Bad")]
    device = Device(code=3, name="Traje", states=states)
    expected_dict = {
        'code': 3,
        'name': 'Traje',
        'states': [{'code': 1, 'name': 'Good'}, {'code': 2, 'name': 'Bad'}]
    }
    assert device.to_dict() == expected_dict
