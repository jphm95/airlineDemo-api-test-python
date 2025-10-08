import os
import requests
import pytest
from utils.settings import BASE_URL, AUTH



@pytest.fixture(scope="session")
def admin_token() -> str:
    user = os.getenv("ADMIN_USER")
    pwd = os.getenv("ADMIN_PASS")

    resp = requests.post(BASE_URL + AUTH,
                         headers={"accept": "application/json",
                                  "Content-Type": "application/x-www-form-urlencoded"},
                         data={"username": user, "password": pwd},
                         timeout=10,
                         )
    resp.raise_for_status()
    return resp.json()["access_token"]

@pytest.fixture
def auth_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            }
