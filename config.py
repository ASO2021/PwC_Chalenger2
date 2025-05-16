import pytest
from api_client import ApiClient

@pytest.fixture(scope="session")
def api():
    client = ApiClient()
    return client

