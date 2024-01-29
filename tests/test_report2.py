from src.models.report2 import Report2

def test_report2_to_dict():
    # Prueba la conversión a un diccionario
    date = "20220127203045"
    mission = "Mission1"
    device = "Device1"
    state = "State1"
    hash_value = "hash123"

    report2 = Report2(date, device, hash_value, mission, state)
    expected_dict = {
        'date': date,
        'mission': mission,
        'device': device,
        'state': state,
        'hash': hash_value
    }

    assert report2.to_dict() == expected_dict
