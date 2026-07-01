from ..src.greet import greet_world, greet_team, greet_fiona, greet_bob, greet_charlie


def test_greet_world():
    assert greet_world() == "Hello, World!"


def test_greet_team():
    assert greet_team("Alpha") == "Hello, Alpha team!"
    
    
def test_greet_charlie():
    assert "Charlie" in greet_charlie("Charlie")



def test_greet_fiona():
    assert "Fiona" in greet_fiona("Fiona")
    result = greet_fiona("Fiona")
    assert isinstance(result, str) 


def test_greet_bob():
    assert "Bob" in greet_bob("Bob")
