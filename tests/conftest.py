import os

import pytest
from flask import Flask

from webapp import create_app


@pytest.fixture()
def app() -> Flask:
    app = create_app()
    app.config.update({
        'TESTING': True
    })

    yield app
    os.close()


@pytest.fixture()
def client(app) -> Flask:
    return app.test_client()


@pytest.fixture
def runner(app) -> Flask:
    return app.test_cli_runner()
