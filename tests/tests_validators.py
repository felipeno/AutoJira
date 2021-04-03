import pytest

from auto_jira.validators import EmailValidator, PasswordValidator


def test_exists_email_validator():
    email_validator = EmailValidator
    assert email_validator is not None


@pytest.mark.parametrize(
    'email',
    [
            '     f@email.com',
            'foo.bar@email.com'
    ]
)
def test_valid_email(email):
    email_validator = EmailValidator(email)
    validator = email_validator.email_validator()
    assert validator[0]


@pytest.mark.parametrize(
    'email',
    [
            '              @email.com',
            '@email.com',
            'foo.baremail.com',
    ]
)
def test_invalid_email(email):
    email_validator = EmailValidator(email)
    validator = email_validator.email_validator('Email inválido: não contém "@" ou está em branco antes do "@".')
    assert not validator[0] and validator[1] == 'Email inválido: não contém "@" ou está em branco antes do "@".'


def test_exists_pass_validator():
    pass_validator = PasswordValidator
    assert pass_validator is not None


@pytest.mark.parametrize(
    'password',
    [
            'foobar',
            '  1'
    ]
)
def test_valid_pass(password):
    pass_validator = PasswordValidator(password)
    validator = pass_validator.password_validator()
    assert validator[0]


@pytest.mark.parametrize(
    'password',
    [
            '',
            '    '
    ]
)
def test_invalid_pass(password):
    pass_validator = PasswordValidator(password)
    validator = pass_validator.password_validator()
    assert not validator[0] and validator[1] == 'Senha inválida: senha em branco.'

