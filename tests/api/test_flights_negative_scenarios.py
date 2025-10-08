import pytest
from dotenv import load_dotenv; load_dotenv()

from utils.support import flights


#Origin | Destination - Tests:
@pytest.mark.parametrize("override, expected_statuses",
 [
    ({"origin": ""},     {400, 422}),
    ({"origin": "123"},  {400, 422}),
    ({"origin": "AB"},   {400, 422}),
    ({"origin": "ABCD"}, {400, 422}),
    ({"origin": 123 },   {400, 422}),
 ],
 ids=["Blank value", "Invalid String - Numbers", "Invalid String - 2 Characters", "Invalid String - 4 Characters", "Invalid Type"]
)
def test_create_flight_invalid_iata_origin(auth_headers, override, expected_statuses ):
    #Action
    body, status = flights.create_flight(auth_headers, override)
    #Assert
    assert status in expected_statuses
    assert "id" not in body

@pytest.mark.parametrize("override, expected_statuses",
 [
    ({"destination": ""},     {400, 422}),
    ({"destination": "123"},  {400, 422}),
    ({"destination": "AB"},   {400, 422}),
    ({"destination": "ABCD"}, {400, 422}),
    ({"destination": 123 },   {400, 422}),
 ],
 ids=["Blank value", "Invalid String - Numbers", "Invalid String - 2 Characters", "Invalid String - 4 Characters", "Invalid Type"]
     )
def test_create_flight_invalid_iata_destination(auth_headers, override, expected_statuses):
    #Action
    body, status = flights.create_flight(auth_headers, override)
    assert status in expected_statuses
    assert "id" not in body

def test_create_flight_destination_and_origin_same_iata_code(auth_headers):
    base_data = flights.build_flight_valid_data(auth_headers)
    origin_code = base_data["origin"]
    overrides = {"origin": origin_code, "destination": origin_code}

    body, status = flights.create_flight(auth_headers, overrides)

    assert status in {400, 422}
    assert "id" not in body

#Dates Tests:
def test_create_flight_past_departure_date(auth_headers):
    past_departure_date = flights.set_past_departure_date()
    overrides = {"departure_time": past_departure_date}

    body, status = flights.create_flight(auth_headers, overrides)

    assert status in {400, 422}
    assert "id" not in body

def test_create_flight_past_arrival_date(auth_headers):
    past_arrival_date = flights.set_past_arrival_date()
    overrides = {"arrival_date": past_arrival_date}

    body, status = flights.create_flight(auth_headers, overrides)

    assert status in {400, 422}
    assert "id" not in body

def test_create_flight_past_departure_and_arrival_date(auth_headers):
    past_departure_date = flights.set_past_departure_date()
    past_arrival_date = flights.set_past_arrival_date()
    overrides = {
        "departure_time": past_departure_date,
         "arrival_time": past_arrival_date
    }

    body, status = flights.create_flight(auth_headers, overrides)

    assert status in {400, 422}
    assert "id" not in body

#Price Tests:
@pytest.mark.parametrize("override, expected_statuses",
 [
    ({"base_price": 0}, {400, 422}),
    ({"base_price": -1}, {400, 422}),
    ({"base_price": 19.99}, {400,422}),
    ({"base_price": 100.01}, {400, 422})
 ],
 ids=["free", "negative_price", "one_unit_below_minimum_limit", "one_unit_above_maximum_limit"]
)
def test_create_flight_invalid_price(auth_headers, override, expected_statuses):
    body, status = flights.create_flight(auth_headers, override)
    assert  status in expected_statuses

#Aircraft
@pytest.mark.parametrize("override, expected_statuses",
[
    ({"aircraft_id": 123456 },  {422}),
    ({"aircraft_id": ""},       {404})

],
ids=["Invalid Id - Type", "Invalid Id - Blank"]
)
def test_create_flight_invalid_aircraft(auth_headers, override, expected_statuses):
    body, status = flights.create_flight(auth_headers, override)
    assert status in expected_statuses
    assert "id" not in body






