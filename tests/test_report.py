from src.models.report import Report
from datetime import datetime

def test_report_initialization():
    # Prueba la inicialización de un informe
    mission = "Mission1"
    device = "Device1"
    state = "State1"

    report = Report(mission, device, state)

    assert report.mission == mission
    assert report.device == device
    assert report.state == state
    assert report.date <= datetime.now().strftime('%Y%m%d%H%M%S')
    assert report.hash == hash((report.date, mission, device, state))

def test_report_unknown_mission():
    # Prueba la inicialización de un informe con misión desconocida
    mission = "Unknown"
    device = "Device1"
    state = "State1"

    report = Report(mission, device, state)

    assert report.mission == mission
    assert report.device == device
    assert report.state == state
    assert report.date <= datetime.now().strftime('%Y%m%d%H%M%S')
    assert report.hash == 0

def test_report_to_dict():
    # Prueba la conversión a un diccionario
    mission = "Mission1"
    device = "Device1"
    state = "State1"

    report = Report(mission, device, state)
    expected_dict = {
        'date': report.date,
        'mission': mission,
        'device': device,
        'state': state,
        'hash': report.hash
    }

    assert report.to_dict() == expected_dict
