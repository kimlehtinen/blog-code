import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()

    yield app

    app.container.unwire()


@pytest.fixture
def client(app):
    return app.test_client()
