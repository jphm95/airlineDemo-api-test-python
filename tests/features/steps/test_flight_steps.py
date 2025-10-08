from behave import given, when, then
from utils.support import flights
import random
import string


@given("I have valid authentication headers")
def step_impl(context):
    context.auth_headers = context.auth_headers

@given("a flight already exists")
def step_impl(context):
    body, status = flights.create_flight(context.auth_headers)
    context.body = body
    context.status = status
    context.flight_id = body["id"]
    context.original_base_price = body.get("base_price")

@given('I generate a valid IATA code and save it as "same_iata"')
def step_impl(context):
    context.same_iata = "".join(random.choices(string.ascii_uppercase, k=3))

@given('I have a past ISO-8601 datetime as "past_departure"')
def step_impl(context):
    context.past_departure = flights.set_past_departure_date()

@given('I have a past ISO-8601 datetime as "past_arrival"')
def step_impl(context):
    context.past_arrival = flights.set_past_arrival_date()


@when("I create a valid flight")
def step_impl(context):
    body, status = flights.create_flight(context.auth_headers)
    context.body = body
    context.status = status

@when("I create a flight overriding:")
def step_impl(context):
    overrides = {row.headings[0]: row.cells[0] for row in context.table}
    body, status = flights.create_flight(context.auth_headers, overrides)
    context.body = body
    context.status = status

@when('I create a flight with an invalid id type:')
def step_impl(context):
    overrides = {row.headings[0]: row.cells[0] for row in context.table}
    body, status = flights.create_flight(context.auth_headers, overrides)
    context.body = body
    context.status = status

@when('I get the flight by "flight_id"')
def step_impl(context):
    body, status = flights.get_flight(context.flight_id, context.auth_headers)
    context.body = body
    context.status = status

@when('I update the flight "flight_id" with a valid change')
def step_impl(context):
    change = {}
    if getattr(context, "original_base_price", None) is not None:
        change["base_price"] = float(context.original_base_price) + 5.0
    body, status = flights.update_flight(context.flight_id, context.auth_headers, overrides=change or None)
    context.body = body
    context.status = status

@when('I delete the flight "flight_id"')
def step_impl(context):
    body, status = flights.delete_flight(context.flight_id, context.auth_headers)
    context.body = body
    context.status = status


@then('I save "id" as "flight_id"')
def step_impl(context):
    context.flight_id = context.body["id"]

@then('the field "id" should equal saved "flight_id"')
def step_impl(context):
    assert context.body["id"] == context.flight_id

@then('the field "base_price" should be different from the original value')
def step_impl(context):
    assert context.body["base_price"] != context.original_base_price

@then('the field "base_price" should equal {price}')
def step_impl(context, price):
    expected = float(price) if "." in str(price) else int(price)
    assert context.body["base_price"] == expected