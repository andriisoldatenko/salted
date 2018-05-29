"""
The idea inspired from django source code :)
Each validator as seperate class to better testing and re usage
"""
import sys


class MinimumLengthValidator:
    """
    Validate whether the password is of a minimum length.
    """
    def __init__(self, min_length=4):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            return False
        return True


class MaximumLengthValidator:
    """
    Validate whether the password is of a maximum length.
    """
    def __init__(self, max_length=6):
        self.max_length = max_length

    def validate(self, password):
        if len(password) > self.max_length:
            return False
        return True


class OneDigitValidator:
    """
    Validate whether the password contains at least 1 digit..
    """
    def validate(self, password):
        if not any(char.isdigit() for char in password):
            return False
        return True


class OneLowerCharValidator:
    """
    Validate whether the password contains at least 1 lower case char.
    """
    def validate(self, password):
        if not any(char.islower() for char in password):
            return False
        return True


class OneUpperCharValidator(object):
    """
    Validate whether the password contains at least 1 UPPER case char.
    """
    def validate(self, password):
        if not any(char.isupper() for char in password):
            return False
        return True


class OneCharacterValidator(object):
    """
    Validate whether the password contains at least
    1 special char from list [*#+@].
    """
    @staticmethod
    def is_punctuation(char):
        return True if char in {'*', '#', '+', '@'} else False

    def validate(self, password):
        if not any(self.is_punctuation(char) for char in password):
            return False
        return True


class NoSpaceValidator(object):
    """
    Validate whether the password contains 0 spaces chars
    """
    def validate(self, password):
        if any(char.isspace() for char in password):
            return False
        return True


def main():
    passwords = sys.stdin.readline().strip().split(',')
    password_validators = [MinimumLengthValidator(),
                           MaximumLengthValidator(),
                           OneDigitValidator(),
                           OneLowerCharValidator(),
                           OneUpperCharValidator(),
                           NoSpaceValidator()]

    valid_passwords = []
    for password in passwords:
        checks = []
        for validator in password_validators:
            if not validator.validate(password):
                checks.append(False)
        if all(checks):
            valid_passwords.append(password)
    print(valid_passwords)


if __name__ == '__main__':
    main()
