import pytest
from api_client import ApiClient  # ajustá esto si tu cliente tiene otro nombre o ruta

@pytest.fixture(scope="module")
def api():
    client = ApiClient()
    yield client
