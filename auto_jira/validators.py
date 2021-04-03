class EmailValidator:
    def __init__(self, email: str):
        self.email = email

    def email_validator(self, msg='') -> list:
        """This method validates if the user's email is valid or not.
        An email whithout '@' or empty before '@' is an invalid email.

        :param msg: str
        :return: tuple
        """
        if '@' not in self.email or not self.email.split('@')[0].strip():
            return [False, msg]

        return [True]


class PasswordValidator:
    def __init__(self, password: str):
        self.password = password

    def password_validator(self) -> list:
        """This method validates if the user's passwords is valida or not.
        An empty password is an invalid password.

        :return: list
        """
        if self.password.strip():
            return [True]
        return [False, 'Senha inválida: senha em branco.']
