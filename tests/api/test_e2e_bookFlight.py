import pytest
from utils.support import flights, bookings, support


def test_e2e_booking_flow(auth_headers):

    # 1) Crear user
    user = support.create_user(auth_headers)

    # 2) Crear Flight
    created_flight, status = flights.create_flight(auth_headers)
    assert status in (200, 201)
    flight_id = created_flight["id"]

    # 3) Create booking
    created_booking = bookings.create_booking(auth_headers)
    booking_id = created_booking["id"]

    # 4) Get booking
    booking = bookings.get_booking(booking_id, auth_headers)

    assert booking["id"] == booking_id
    assert booking["user_id"] == user["id"]
    assert booking["flight_id"] == flight_id
    assert len(booking["passengers"]) > 0

    #Clean Test
    delete_booking_status = bookings.delete_booking(booking_id, auth_headers)
    assert delete_booking_status in (200, 204)

    delete_flight_status = flights.delete_flight(flight_id, auth_headers)
    assert delete_flight_status in (200, 204)