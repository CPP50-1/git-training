from src.greet import greet_world


def test_greet_world():
    assert greet_world() == "Hello, World!"