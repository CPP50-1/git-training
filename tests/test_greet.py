from ..src.greet import (
    greet_evan,
    greet_george,
    greet_georges,
    greet_julia,
    greet_karl,
    greet_world,
    greet_team,
    greet_fiona,
    greet_bob,
    greet_charlie,
    greet_hannah,
)


def test_greet_world():
    assert greet_world() == "Hello, World!"


def test_greet_team():
    assert greet_team("Alpha") == "Hello, Alpha team!"


def test_greet_charlie():
    assert "Charlie" in greet_charlie("Charlie")


def test_greet_julia():
    assert greet_julia("Julia") == "Hey Julia, have a nice day!"


def test_greet_fiona():
    assert "Fiona" in greet_fiona("Fiona")
    result = greet_fiona("Fiona")
    assert isinstance(result, str)


def test_greet_hannah():
    assert "Hannah" in greet_hannah("Hannah")
    result = greet_hannah("Hannah")
    assert isinstance(result, str)


def test_greet_bob():
    assert "Bob" in greet_bob("Bob")


def test_greet_karl():
    """checks whether the name provided to the function is in the return"""
    assert "Denis" in greet_karl("Denis")


def test_greet_george():
    assert "George" in greet_george("George")


def test_greet_georges():
    assert "Georges" in greet_georges("Georges")


def test_greet_evan():
    assert "Evan" in greet_evan("Evan")
