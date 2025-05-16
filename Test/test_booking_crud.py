from Data.sample_payloads import generate_booking

def test_create_booking(api):
    booking_data = generate_booking()
    response = api.create_booking(booking_data)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    retrieved = api.get_booking(booking_id)
    assert retrieved.status_code == 200
    assert retrieved.json()["firstname"] == booking_data["firstname"]

def test_update_booking(api):
    booking_data = generate_booking()
    create_response = api.create_booking(booking_data)
    booking_id = create_response.json()["bookingid"]
    api.authenticate()
    updated_data = booking_data.copy()
    updated_data["firstname"] = "UpdatedName"
    update_response = api.update_booking(booking_id, updated_data, api.token)
    assert update_response.status_code == 200
    get_response = api.get_booking(booking_id)
    assert get_response.json()["firstname"] == "UpdatedName"

def test_unauthorized_update(api):
    booking_data = generate_booking()
    create_response = api.create_booking(booking_data)
    booking_id = create_response.json()["bookingid"]
    updated_data = booking_data.copy()
    updated_data["lastname"] = "Hacked"
    response = api.update_booking(booking_id, updated_data, token="invalidtoken")
    assert response.status_code == 403

def test_delete_booking(api):
    booking_data = generate_booking()
    create_response = api.create_booking(booking_data)
    booking_id = create_response.json()["bookingid"]
    api.authenticate()
    delete_response = api.delete_booking(booking_id, api.token)
    assert delete_response.status_code == 201
    get_response = api.get_booking(booking_id)
    assert get_response.status_code == 404

def test_unauthorized_delete(api):
    booking_data = generate_booking()
    create_response = api.create_booking(booking_data)
    booking_id = create_response.json()["bookingid"]
    delete_response = api.delete_booking(booking_id, token="invalidtoken")
    assert delete_response.status_code == 403

def test_partial_update(api):
    booking_data = generate_booking()
    create_response = api.create_booking(booking_data)
    booking_id = create_response.json()["bookingid"]
    api.authenticate()
    patch_data = {"firstname": "Partial"}
    patch_response = api.partial_update_booking(booking_id, patch_data, api.token)
    assert patch_response.status_code == 200
    get_response = api.get_booking(booking_id)
    assert get_response.json()["firstname"] == "Partial"
    assert get_response.json()["lastname"] == booking_data["lastname"]
