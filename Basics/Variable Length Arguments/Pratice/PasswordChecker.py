def is_strong(password):
    """
    Check if the given password is strong.

    A strong password must meet the following criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character (e.g., !, @, #, $, etc.)

    Args:
        password (str): The password to check.
    """
    if len(password) < 8:
        return False , "Password must be at least 8 characters long."

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if not has_upper:
        return False , "Password must contain at least one uppercase letter."

    if not has_lower:
        return False , "Password must contain at least one lowercase letter."

    if not has_digit:
        return False , "Password must contain at least one digit."

    if not has_special:
        return False , "Password must contain at least one special character."

    return True , "Password is strong!"

print(is_strong("Password123!"))  # True