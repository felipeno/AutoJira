"""
This module contains the controller's functions.
This is the local where the inputs of the view are interpreted, processed and answered.
"""
from auto_jira.model.service.validators import EmailValidator, PasswordValidator


class Controller:
    @classmethod
    def emails_validator(cls, emails: list) -> bool:
        """This method call the email validator that return in a bool if the emails are valid emails or not.

        :param emails: list
        :return: bool
        """
        return EmailValidator(emails).emails_validator()

    @classmethod
    def passwords_validator(cls, passwords: list) -> bool:
        """This method call the password validator that return in a bool if the passwords are valid passwords or not.

        :param passwords: list
        :return: bool
        """
        return PasswordValidator(passwords).passwords_validator()
