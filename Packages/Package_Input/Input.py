from Packages.Package_Input.Validate import validate_number,check_max_length,check_min_length
from Packages.Package_System.system import clear_screen

def get_int(message: str, error_message = "Error", attempts = 0, min = True, max = True,) -> int|None:
    """Obtains an integer from the user.

    Args:
        message (str): The prompt for user input.
        error_message (str): The error message to display if validation fails.
        min (int): The minimum value for the number's range. (Optional)
        max (int): The maximum value for the number's range. (Optional)
        attempts (int): The number of attempts allowed for user input. (Optional)

    Returns:
        int|None: Returns an interger if succesfull, or None otherwise.
    """
    attempt = 1
    number = input(message)
    while not validate_number(number=number, min=min, max=max):
        if attempt == attempts:
            number = None
            break
        print(error_message)
        input("Presione una tecla para continuar..\n")
        clear_screen()
        number = input(message)
        attempt +=1        
    if number != None:
        number = int(number)
    return number

def get_float(message: str, error_message = "Error",  attempts = 0, min = True, max = True) -> float|None:
    """Obtains a float from the user

    Args:
        message (str): The prompt for user input.
        error_message (str): The error message to display if validation fails.
        min (float): The minimum value for the number's range. (Optional)
        max (float): The maximum value for the number's range. (Optional)
        attempts (float): The number of attempts allowed for user input. (Optional)

    Returns:
        float|None: Returns a float if succesfull, or None otherwise.
    """
    attempt = 1
    number = input(message)
    number = float(number)
    while not validate_number(number=number, min=min, max=max):
        if attempt == attempts:
            number = None
            break
        else:
            pass
        print(error_message)
        number = input(message)
        number = float(number)
        attempt +=1
        
    return number

def get_string( message: str, max_length = True , min_length = True) -> str:
    """Obtains a string from the user

    Args:
        message (str): The prompt for user input.
        max_length (int): Maximum length of the string. (Optional)

    Returns:
        str|None: Returns a string.
    """
    text = input(message)
    if type(max_length) == int or (max_length) == int:
        while not check_max_length(max_length, text) or not check_min_length(min_length,text):
            if type(min_length) == int and type(max_length) == int:
                print(f"El texto debe tener por lo menos {min_length} caracteres y {max_length} como maximo")
            elif type(min_length) == int:
                print(f"El texto debe tener por lo menos {min_length} caracteres")
            else:
                print(f"El texto debe tener {max_length} como maximo")
            text = input(message)
    return text

def get_confirm(message="¿Desea confirmar? [S/n]\n") -> bool:
    """Ask the user for an input. Returns a bool.

    Args:
        message (str, optional): Message that's printed to the user. Defaults to "¿Desea confirmar? [S/n]\n".

    Returns:
        bool: True if "s", False if "n"
    """
    options = ["s","n"]
    option = get_string(message=message,min_length=1,max_length=1)
    option = option.lower()
    while option not in options:
        option = get_string(message=message,min_length=1,max_length=1)
        option = option.lower()
    return option == "s"