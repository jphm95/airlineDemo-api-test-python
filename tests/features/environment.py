import os
import requests
from utils.settings import BASE_URL, AUTH

def before_all(context):
    user = os.getenv("ADMIN_USER")
    pwd = os.getenv("ADMIN_PASS")

    response = requests.post(
        BASE_URL + AUTH,
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={"username": user, "password": pwd},
        timeout=10
    )
    response.raise_for_status()
    context.admin_token = response.json()["access_token"]
    context.auth_headers = {
        "Authorization": f"Bearer {context.admin_token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    context.base_url = BASE_URL