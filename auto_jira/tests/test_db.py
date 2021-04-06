# pytest auto_jira --cov-report term-missing --cov=auto_jira
import os
import pytest
from auto_jira.model.service.validators import DataBaseValidator
from auto_jira.model.persistence.db import DataBaseConnection

PATH_TEST = 'foobar.db'


@pytest.fixture()
def connection_obj():
    db_conn_obj = DataBaseConnection(PATH_TEST)
    yield db_conn_obj
    db_conn_obj.create_connection()
    db_conn_obj.close_connection()
    os.remove(PATH_TEST)


def test_inexists_test_db():
    db = DataBaseValidator(PATH_TEST)
    check = db.exist_validator()
    assert not check


def test_exists_test_db(connection_obj):
    connection_obj.create_connection()

    db_validator = DataBaseValidator(PATH_TEST)
    check = db_validator.exist_validator()
    assert check


def test_create_test_db_because_test_db_doesnt_exists(connection_obj):
    conn = None

    db_validator = DataBaseValidator(PATH_TEST)
    if not db_validator.exist_validator():
        conn = connection_obj.create_connection()

    assert conn
