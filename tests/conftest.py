import pytest
from api.v1.app_init import create_app


@pytest.fixture  # app fixture
def app():
    app = create_app()

    yield app  # return app instance

@pytest.fixture # client fixture to be used when testing
def client(app):
    return app.test_client()


