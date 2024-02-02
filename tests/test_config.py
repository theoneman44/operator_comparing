from flask import Flask


def test_testing_config(app: Flask, database_url_env_var: str) -> None:
    assert app.config['SQLALCHEMY_DATABASE_URI'] == database_url_env_var
    assert app.config['TESTING']


def test__env(database_url_env_var) -> None:
    assert 'tarifs_test' in database_url_env_var
