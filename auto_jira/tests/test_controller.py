import pytest

from auto_jira.controller.controller import Controller


@pytest.mark.parametrize(
    'email',
    [
            '     f@email.com',
            'foo.bar@email.com',
            '              @email.com',
            '@email.com',
            'foo.baremail.com',
    ]
)
def test_controller_email_validator_return_a_bool(email):
    assert isinstance(Controller.emails_validator([email]), bool)


@pytest.mark.parametrize(
    'password',
    [
            'foobar',
            '  1',
            '',
            '    '
    ]
)
def test_controller_password_validator_return_a_bool(password):
    assert isinstance(Controller.passwords_validator([password]), bool)

