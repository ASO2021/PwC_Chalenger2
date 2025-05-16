import requests

class ApiClient:
    def __init__(self):
        self.base_url = "https://restful-booker.herokuapp.com"
        self.token = None

    def authenticate(self):
        url = f"{self.base_url}/auth"
        data = {
            "username": "admin",
            "password": "password123"
        }
        response = requests.post(url, json=data)
        response.raise_for_status()
        self.token = response.json().get("token")
        return self.token

    def create_booking(self, booking_data):
        url = f"{self.base_url}/booking"
        response = requests.post(url, json=booking_data)
        return response

    def get_booking(self, booking_id):
        url = f"{self.base_url}/booking/{booking_id}"
        response = requests.get(url)
        return response

    def update_booking(self, booking_id, booking_data, token):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {"Cookie": f"token={token}"}
        response = requests.put(url, json=booking_data, headers=headers)
        return response

    def partial_update_booking(self, booking_id, patch_data, token):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {"Cookie": f"token={token}"}
        response = requests.patch(url, json=patch_data, headers=headers)
        return response

    def delete_booking(self, booking_id, token):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {"Cookie": f"token={token}"}
        response = requests.delete(url, headers=headers)
        return response
