import os
import pytest
from flask import Flask
from werkzeug.test import TestResponse
from webapp import create_app, db
'''
Варианты GET запросов
/?mobile_operator_name=Мегафон&phone_internet_quantity=5&phone_minutes_quantity=200&phone_sms_quantity=50
/?mobile_operator_name=0&phone_internet_quantity=30&unlim_phone_internet=1&phone_minutes_quantity=1000&unlim_phone_minutes=1&phone_sms_quantity=250
/?mobile_operator_name=МТС&phone_internet_quantity=30&phone_minutes_quantity=1000&phone_sms_quantity=250

/all_in?mobile_operator_name=0&phone_internet_qty=30&phone_minutes_qty=1000&internet_speed=400&channels_qty=200
'''


@pytest.fixture(scope="module")
def database_url_env_var() -> pytest.fixture():
    basedir = os.path.abspath(os.path.dirname(__file__))
    os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'tarifs_test.db')
    return os.environ['SQLALCHEMY_DATABASE_URI']


@pytest.fixture(scope="module")
def app(database_url_env_var) -> Flask:
    app = create_app()
    app.config.update({
        'TESTING': True,
    })
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url_env_var
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app) -> Flask:
    return app.test_client()


@pytest.fixture()
def runner(app) -> Flask:
    return app.test_cli_runner()


@pytest.fixture()
def query(client: Flask) -> TestResponse:
    request = client.get(path='/', query_string={'mobile_operator_name': 0, 'phone_internet_quantity': 20, 'phone_minutes_quantity': 400, 'phone_sms_quantity': 50})
    return request
