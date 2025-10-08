Feature: Flights API
  Manage flights lifecycle and validate input rules (IATA, dates, price, aircraft).

  Background:
    Given I have valid authentication headers

  @smoke @create
  Scenario: Create flight successfully
    When I create a valid flight
    Then the response status should be 201
    And the response body should contain "id"
    And I save "id" as "flight_id"

  @smoke @get
  Scenario: Get flight by id
    Given a flight already exists
    When I get the flight by "flight_id"
    Then the response status should be 200
    And the field "id" should equal saved "flight_id"

  @smoke @update
  Scenario: Update flight successfully
    Given a flight already exists
    When I update the flight "flight_id" with a valid change
    Then the response status should be 200
    And the field "id" should equal saved "flight_id"
    And the field "base_price" should be different from the original value

  @smoke @delete
  Scenario: Delete flight successfully
    Given a flight already exists
    When I delete the flight "flight_id"
    Then the response status should be 204


  #Valid Price Test

  @price @positive @boundary
  Scenario Outline: Create flight with valid price
    When I create a flight overriding:
      | base_price | <price> |
    Then the response status should be 201
    And the response body should contain "id"
    And the field "base_price" should equal <price>

    Examples:
      | price  |
      | 20     |
      | 20.01  |
      | 60     |
      | 99.99  |
      | 100    |

  # Invalid IATA codes for origin

  @iata @negative
  Scenario Outline: Create flight with invalid origin
    When I create a flight overriding:
      | origin | <origin> |
    Then the response status should be one of:
      | 400 |
      | 422 |
    And the response body should not contain "id"

    Examples:
      | origin |
      |        |
      | 123    |
      | AB     |
      | ABCD   |
      | 123.0  |


  # Invalid IATA codes for destination

  @iata @negative
  Scenario Outline: Create flight with invalid destination
    When I create a flight overriding:
      | destination | <destination> |
    Then the response status should be one of:
      | 400 |
      | 422 |
    And the response body should not contain "id"

    Examples:
      | destination |
      |             |
      | 123         |
      | AB          |
      | ABCD        |
      | 123.0       |


  # Origin equals Destination

  @iata @negative
  Scenario: Create flight when origin and destination are the same
    Given I generate a valid IATA code and save it as "same_iata"
    When I create a flight overriding:
      | origin      | <same_iata> |
      | destination | <same_iata> |
    Then the response status should be one of:
      | 400 |
      | 422 |
    And the response body should not contain "id"


  #Past dates

  @dates @negative
  Scenario: Create flight with past departure date
    Given I have a past ISO-8601 datetime as "past_departure"
    When I create a flight overriding:
      | departure_time | <past_departure> |
    Then the response status should be one of:
      | 400 |
      | 422 |
    And the response body should not contain "id"

  @dates @negative
  Scenario: Create flight with past arrival date
    Given I have a past ISO-8601 datetime as "past_arrival"
    When I create a flight overriding:
      | arrival_time | <past_arrival> |
    Then the response status should be one of:
      | 400 |
      | 422 |
    And the response body should not contain "id"

  @dates @negative
  Scenario: Create flight with past departure and arrival dates
    Given I have a past ISO-8601 datetime as "past_departure"
    And I have a past ISO-8601 datetime as "past_arrival"
    When I create a flight overriding:
      | departure_time | <past_departure> |
      | arrival_time   | <past_arrival>   |
    Then the response status should be one of:
      | 400 |
      | 422 |
    And the response body should not contain "id"


  #Invalid price (negative/zero/out of range)

  @price @negative @boundary
  Scenario Outline: Create flight with invalid price
    When I create a flight overriding:
      | base_price | <price> |
    Then the response status should be one of:
      | 400 |
      | 422 |
    And the response body should not contain "id"

    Examples:
      | price  |
      | 0      |
      | -1     |
      | 19.99  |
      | 100.01 |


  # Invalid aircraft

  @aircraft @negative
  Scenario Outline: Create flight with invalid aircraft id
    When I create a flight with an invalid id type:
      | aircraft_id | <aircraft> |
    Then the response status should be one of:
      | 404 |
      | 422 |
    And the response body should not contain "id"

    Examples:
      | aircraft |
      | 123456   |

