import requests

def login_user(api_url, username, password):
    response = requests.post(f"{api_url}/login", json={
        "username": username,
        "password": password
    })
    response.raise_for_status()
    return response.json()
