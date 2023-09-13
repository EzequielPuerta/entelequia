from typing import Callable

import pytest
from flask.testing import FlaskClient

from entelequia.flask.entelequia import Entelequia
from entelequia.modules import time
from entelequia.system.module import Module

from .app import create_app


@pytest.fixture(scope="session")
def app_factory() -> Callable[[set[Module]], Entelequia]:
    def _app_factory(modules: set[Module]) -> Entelequia:
        app = create_app(__name__, modules=modules)
        app.config.update(
            {
                "TESTING": True,
            }
        )
        return app

    yield _app_factory


@pytest.fixture(scope="session")
def app(app_factory: Callable[[set[Module]], Entelequia]) -> Entelequia:
    app = app_factory(modules=set((time.module,)))
    app.time_system = time.module.system

    @app.route("/")
    def hello():
        return "Hello, World!"

    yield app


@pytest.fixture(scope="session")
def client(app: Entelequia) -> FlaskClient:
    yield app.test_client()
