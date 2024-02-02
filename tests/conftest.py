import os
import pytest
from flask import Flask
from webapp import create_app, db


@pytest.fixture(scope="module")
def database_url_env_var() -> pytest.fixture():
    basedir = os.path.abspath(os.path.dirname(__file__))
    database_url = 'sqlite:///' + os.path.join(basedir, '..', 'tarifs_test.db')
    return database_url


@pytest.fixture(scope="module")
def app(database_url_env_var) -> Flask:
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': database_url_env_var,
    })

    with app.app_context():
        db.init_app(app)
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app) -> Flask:
    return app.test_client()
