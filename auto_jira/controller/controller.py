from auto_jira.model.service.validators import EmailValidator, PasswordValidator


class Controller:
    @classmethod
    def emails_validator(cls, emails):
        return EmailValidator(emails).emails_validator()

    @classmethod
    def passwords_validator(cls, passwords):
        return PasswordValidator(passwords).passwords_validator()