import random

from utils.api_helpers import api_request
from utils.settings import BASE_URL, BOOKINGS
from utils import support
from utils.support import flights


def create_booking(auth_headers):
    user = support.create_user(auth_headers)
    flight_json, _ = flights.create_flight(auth_headers)
    flight_id = flight_json["id"]
    booking_data = {
        "flight_id": flight_id,
        "user_id": user["id"],
        "status": "paid",
        "passengers": [
            {
                "full_name": user["full_name"],
                "passport": "".join(random.choices(string.ascii_uppercase + string.digits, k=9)),
                "seat": f"{random.randint(1, 30)}{random.choice('ABCDEF')}"
            }
        ]
    }

    r = api_request("post",  BOOKINGS, json=booking_data, headers=auth_headers)
    r.raise_for_status()
    return r.json()

def update_booking(booking_id, auth_headers):
    booking_data = {
        "origin": "MXN",
        "destination": "AGU",
        "departure_time": "2025-09-14T02:49:53.414Z",
        "arrival_time": "2025-09-14T02:49:53.414Z",
        "base_price": 0,
        "aircraft_id": "string"
    }

    r = api_request("put", BOOKINGS + f"/{booking_id}", json=booking_data, headers=auth_headers)
    r.raise_for_status()
    return r.json()

def  get_bookings(auth_headers):
    r = api_request("get", BOOKINGS, headers=auth_headers)
    r.raise_for_status()
    return r.json()


def  get_booking(booking_id, auth_headers):
    r = api_request("get", BOOKINGS + f"/{booking_id}", headers=auth_headers)
    r.raise_for_status()
    return r.json()

def  delete_booking(booking_id, auth_headers):
    r = api_request("delete", BOOKINGS + f"/{booking_id}", headers=auth_headers)
    r.raise_for_status()
    return r.status_code