class EmailValidator:
    def __init__(self, emails: list):
        self.emails = emails

    def emails_validator(self) -> bool:
        """This method validates if the user's email is valid or not.
        An email whithout '@' or empty before '@' is an invalid email.

        :param msg: str
        :return: tuple
        """
        for email in self.emails:
            if '@' not in email or not email.split('@')[0].strip():
                return False

        return True


class PasswordValidator:
    def __init__(self, passwords: list):
        self.passwords = passwords

    def passwords_validator(self) -> bool:
        """This method validates if the user's passwords is valida or not.
        An empty password is an invalid password.

        :return: list
        """
        for password in self.passwords:
            if not password.strip():
                return False
        return True
