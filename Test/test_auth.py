def test_valid_authentication(api):
    response = api.authenticate()
    assert response.status_code == 200
    assert "token" in response.json()

def test_invalid_authentication(api):
    response = api.authenticate("invalid", "wrong")
    assert response.status_code == 403
