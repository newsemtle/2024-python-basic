from dataclasses import dataclass


@dataclass
class SaveData:
    gold: int
    inventory: list
    allies: list
    enemies: list
    current_location: int


def get_save_dir():
    import os
    import sys

    # get executable path
    if getattr(sys, "frozen", False):
        # if the script is running as a standalone executable
        executable_dir = os.path.dirname(sys.executable)
    else:
        executable_dir = os.path.dirname(os.path.dirname(__file__))

    return executable_dir + r"\save"


def save(gm, location):
    pass


def has_save_file():
    pass


def load_data():
    pass
