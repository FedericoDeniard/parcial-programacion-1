def validate_number(number: str, min =  True, max = True) -> bool :
    """Validates the range of an interger.

    Args:
        min (int): The minimum value for the number's range. (Optional)
        max (int): The maximum value for the number's range. (Optional)
        number (int): The number of attempts allowed for user input.

    Returns:
        _type_: True or False depending on the number's range.
    """
    is_valid = True
    if number.isdigit():
        number = int(number)
        if type(min) != bool or type(max) != bool:
            if number < min or number > max:
                is_valid = False
    else:
        is_valid = False

    return is_valid


def check_max_length(max_length: int, text: str) -> bool:
    is_valid = True
    if len(text) > max_length:
        is_valid = False
        
    return is_valid

def check_min_length(min_length: int, text: str) -> bool:
    is_valid = True
    if len(text) < min_length:
        is_valid = False
        
    return is_valid