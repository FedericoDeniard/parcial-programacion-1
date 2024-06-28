import platform
from os import system

def clear_screen():
    """Clears the screen, depending on your os system. Only Windows and Linux are supported."""
    os_name = platform.system()
    if os_name == "Windows":
        system("cls")
    else:
        system("clear")