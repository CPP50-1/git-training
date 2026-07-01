from src.greet import greet_world, greet_team


def test_greet_world():
    assert greet_world() == "Hello, World!"


def test_greet_team():
    assert greet_team("Alpha") == "Hello, Alpha team!"
