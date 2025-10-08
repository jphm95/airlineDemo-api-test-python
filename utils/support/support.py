from utils.api_helpers import api_request
from utils.settings import  AIRCRAFTS, USERS
import random
from faker import Faker
import string



def ensure_aircraft_id(auth_headers):
    aircraft_data = {
        "tail_number": "".join(random.choices(string.ascii_uppercase, k=random.randint(5, 10))),
        "model": 	random.choice(["AIRBUS", "BOEING", "EMBRAER"] ),
        "capacity": random.randint(100, 160)
    }

    r = api_request("post", AIRCRAFTS, json=aircraft_data, headers=auth_headers)
    r.raise_for_status()
    aircraft_created = r.json()
    return aircraft_created["id"]

def create_user(auth_headers):
    faker = Faker()
    user_data = {
        "email": f"{random.choice(string.ascii_lowercase)}@{random.choice(string.ascii_lowercase)}.com",
        "password": random.choice(string.ascii_lowercase),
        "full_name": faker.name(),
        "role": "passenger"
    }

    r = api_request("post", USERS, json=user_data, headers=auth_headers)
    r.raise_for_status()
    user_created = r.json()
    return {
        "id": user_created["id"],
        "full_name": user_created["full_name"]
    }

