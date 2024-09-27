class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


SPECIAL_CHARS = ['@', '&', '*', '%']
password = input()

while password != "Done":

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password.isalpha() or password.isdigit() or all(x in SPECIAL_CHARS for x in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(x in SPECIAL_CHARS for x in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")

    password = input()

