"""Q5. TYPE CONVERSION SAFETY
    Write a function safe_to_int(value) that:
    - Takes ANY value (str, float, bool, None, etc.)
    - Attempts to convert it to int
    - Returns the int if successful
    - Returns None if conversion fails (don't let it crash!)
    - Returns 0 for None input specifically
    Test with: "42", "3.7", "hello", True, None, [], "  15  ", "0xFF
"""

def safe_to_int(value):

    if type(value) == int:
        return value
    elif type(value) == bool:
        return int(value)
    elif type(value) == float:
        return int(value)
    elif value is None:
        return 0
    else:
        return None

converted_value = safe_to_int(6373.83899)
print(converted_value)