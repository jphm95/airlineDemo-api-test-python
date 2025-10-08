import pytest
from dotenv import load_dotenv; load_dotenv()

from utils.support import flights

#Create, Get, Update, Delete Flight - Smoke:
def test_create_flight(auth_headers):
    #Act
    created_flight, status = flights.create_flight(auth_headers)

    #Assert
    assert isinstance(created_flight, dict)
    assert created_flight.get("id")
    assert status == 201

def test_get_flight(auth_headers):
    #Arrange
    created_flight, status = flights.create_flight(auth_headers)
    flight_id = created_flight["id"]

    #Act
    flight, status = flights.get_flight(flight_id, auth_headers)

    #Assert
    assert flight["id"] == flight_id
    assert status == 200

def test_update_flight(auth_headers):
    # Arrange
    create_flight, status = flights.create_flight(auth_headers)
    flight_id = create_flight["id"]

    #Act
    flight, status = flights.update_flight(flight_id, auth_headers)

    #Assert
    assert flight["id"] == flight_id
    assert flight["base_price"] != create_flight["base_price"]
    assert status == 200

def test_delete_flight(auth_headers):
    # Arrange
    created_flight, status = flights.create_flight(auth_headers)
    flight_id = created_flight["id"]

    #Act
    flight, status = flights.delete_flight(flight_id, auth_headers)

    #Assert
    assert status == 204


#Price Test:
@pytest.mark.parametrize("override, expected_status",
[
    ({"base_price": 20},     {201}),
    ({"base_price": 20.01},  {201}),
    ({"base_price": 60},     {201}),
    ({"base_price": 99.99},    {201}),
    ({"base_price": 100},    {201})
],
    ids=["valid_minimum_limit", "one_unit_above_minimum_limit", "mid_range_unit",
         "one_unit_below_maximum_limit", "maximum_limit"]
    )
def test_create_flight_valid_price(auth_headers, override, expected_status):
    body, status = flights.create_flight(auth_headers, override)
    assert status in expected_status
    assert body["base_price"] == override["base_price"]
