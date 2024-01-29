from src.data.data import get_data
from src.models.device import Device
from src.models.mission import Mission
from src.models.state import State

def test_get_data_returns_list():
    result = get_data()
    assert isinstance(result, list), "La función get_data() debe devolver una lista"

def test_get_data_mission_structure():
    result = get_data()
    assert all(isinstance(mission, Mission) for mission in result), "La función get_data() debe devolver instancias de Mission"
    assert all(hasattr(mission, 'devices') for mission in result), "Las instancias de Mission deben tener el atributo 'devices'"

def test_get_data_device_structure():
    result = get_data()
    devices = [device for mission in result for device in mission.devices]
    assert all(isinstance(device, Device) for device in devices), "La función get_data() debe devolver instancias de Device"
    assert all(hasattr(device, 'states') for device in devices), "Las instancias de Device deben tener el atributo 'states'"
