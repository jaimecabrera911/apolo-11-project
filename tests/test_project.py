from src.models.project import Project
from src.models.mission import Mission
from src.models.device import Device

def test_project_initialization():
    # Prueba la inicialización de un proyecto
    missions = [
        Mission(code="ORBONE", name="OrbitOne"),
        Mission(code="CLNM", name="ColonyMoon"),
        Mission(code="TMRS", name="VacMars")
    ]
    project = Project(code="APOLLO", name="Apollo 11", missions=missions)

    assert project.code == "APOLLO"
    assert project.name == "Apollo 11"
    assert project.missions == missions

def test_project_initialization_with_empty_missions():
    # Prueba la inicialización de un proyecto con una lista vacía de misiones
    project = Project(code="APOLLO", name="Apollo 11", missions=[])

    assert project.code == "APOLLO"
    assert project.name == "Apollo 11"
    assert project.missions == []
