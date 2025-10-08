import datetime
import string
import random
from datetime import datetime, timedelta, timezone


from utils.api_helpers import api_request
from utils.settings import FLIGHTS
from utils import support



def build_flight_valid_data(auth_headers, overrides=None):
    departure = datetime.now(timezone.utc) + timedelta(hours=2)
    arrival = departure + timedelta(hours=1.5)
    flight_data = {
        "origin": "".join(random.choices(string.ascii_uppercase, k=3)),
        "destination": "".join(random.choices(string.ascii_uppercase, k=3)),
        "departure_time": departure.isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "arrival_time": arrival.isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "base_price": random.uniform(20, 100),
        "aircraft_id": support.ensure_aircraft_id(auth_headers)
    }
    if overrides:
        flight_data.update(overrides)
    return flight_data


def create_flight(auth_headers, overrides=None):
    flight_data = build_flight_valid_data(auth_headers)
    if overrides:
        flight_data.update(overrides)

    r = api_request("post", FLIGHTS, json=flight_data, headers=auth_headers)
    return r.json(), r.status_code

def update_flight(flight_id, auth_headers):
    flight_data = build_flight_valid_data(auth_headers, {"base_price": random.uniform(20, 100)})
    r = api_request("put", FLIGHTS + f"/{flight_id}", json=flight_data, headers=auth_headers)
    return r.json(), r.status_code


def  get_flight(flight_id, auth_headers):
    r = api_request("get", FLIGHTS + f"/{flight_id}", headers=auth_headers)
    r.raise_for_status()
    return  r.json(), r.status_code

def  delete_flight(flight_id, auth_headers):
    r = api_request("delete", FLIGHTS + f"/{flight_id}", headers=auth_headers)
    r.raise_for_status()
    return r.status_code

def set_past_departure_date():
    now_utc = datetime.now(timezone.utc)
    past_departure = (now_utc - timedelta(days=2)).replace(microsecond=0)
    dep_iso = past_departure.isoformat().replace("+00:00", "Z")
    return dep_iso

def set_past_arrival_date():
    past_departure = set_past_departure_date()
    past_arrival = datetime.fromisoformat(past_departure.replace("Z", "+00:00")) + timedelta(hours=2)
    arr_iso = past_arrival.isoformat(timespec="seconds").replace("+00:00", "Z")
    return arr_iso