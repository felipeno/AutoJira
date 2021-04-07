import os

import pytest

from auto_jira.model.persistence.db import DataBaseConnection
from auto_jira.model.service.validators import EmailValidator, PasswordValidator, DataBaseValidator
from auto_jira.tests.test_db import PATH_TEST


@pytest.fixture()
def connection_obj():
    db_conn_obj = DataBaseConnection(PATH_TEST)
    yield db_conn_obj
    db_conn_obj.create_connection()
    db_conn_obj.close_connection()
    os.remove(PATH_TEST)


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
    email_validator = EmailValidator([email])
    validator = email_validator.emails_validator()
    assert validator


@pytest.mark.parametrize(
    'email',
    [
            '              @email.com',
            '@email.com',
            'foo.baremail.com',
    ]
)
def test_invalid_email(email):
    email_validator = EmailValidator([email])
    validator = email_validator.emails_validator()
    assert not validator


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
    pass_validator = PasswordValidator([password])
    validator = pass_validator.passwords_validator()
    assert validator


@pytest.mark.parametrize(
    'password',
    [
            '',
            '    '
    ]
)
def test_invalid_pass(password):
    pass_validator = PasswordValidator([password])
    validator = pass_validator.passwords_validator()
    assert not validator


def test_exists_test_db_table(connection_obj):
    database_validator_obj = DataBaseValidator(PATH_TEST)
    connection_obj.create_connection()
    cursor_obj = connection_obj.create_cursor()
    cursor_obj.create_table('test')
    check = database_validator_obj.exists_table_validator(cursor_obj.cursor, 'test')
    assert check


def test_inexists_test_db_table(connection_obj):
    database_validator_obj = DataBaseValidator(PATH_TEST)
    connection_obj.create_connection()
    cursor_obj = connection_obj.create_cursor()
    check = database_validator_obj.exists_table_validator(cursor_obj.cursor, 'test')
    assert not check
