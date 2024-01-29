from src.models.state import State

def test_state_initialization():
    # Prueba la inicialización de una instancia de State
    code = 1
    name = "Excellent"
    
    state = State(code, name)

    assert state.code == code
    assert state.name == name
