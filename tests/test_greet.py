from src.greet import greet_world, greet_team, greet_fiona, greet_alice

def test_greet_world():
    assert greet_world() == "Hello, World!"


def test_greet_team():
    assert greet_team("Alpha") == "Hello, Alpha team!"

def test_greet_alice():
    assert greet_alice("Alice") == "Hey Alice, glad you're here!"

def test_greet_fiona():
    assert "Fiona" in greet_fiona("Fiona")
    result = greet_fiona("Fiona")
    assert isinstance(result, str) 
