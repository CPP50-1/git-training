"""
Greeting module, each developer adds one greet_<name> function below.
The function must accept a `name: str` argument and return a greeting string.
"""


def greet_world() -> str:
    """Default greeting, already implemented as an example."""
    return "Hello, World!"


def greet_team(team_name: str) -> str:
    """Greet an entire team."""
    return f"Hello, {team_name} team!"

def greet_alice(name: str) -> str:
    """Alice's personal greeting."""
    return f"Hey {name}, glad you're here!"