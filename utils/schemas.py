
#FLIGHTS:
flightCreate = {
    "type": "object",
    "required": ["origin", "destination", "departure_time", "arrival_time", "base_price", "aircraft_id"],
    "properties": {
        "origin": {"type": "string", "minLength": 3, "maxLength": 3},
        "destination": {"type": "string", "minLength": 3, "maxLength": 3},
        "departure_time": {"type": "string", "format": "date-time"},
        "arrival_time": {"type": "string", "format": "date-time"},
        "base_price": {"type": "number"},
        "aircraft_id": {"type": "string"}
    },
    "additionalProperties": False
}

flightOut = {
    "type": "object",
    "required": ["id", "origin", "destination", "departure_time", "arrival_time", "base_price", "aircraft_id"],
    "properties": {
        "id": {"type": "string"},
        "origin": {"type": "string", "minLength": 3, "maxLength": 3},
        "destination": {"type": "string", "minLength": 3, "maxLength": 3},
        "departure_time": {"type": "string", "format": "date-time"},
        "arrival_time": {"type": "string", "format": "date-time"},
        "base_price": {"type": "number"},
        "aircraft_id": {"type": "string"},
        "available_seats": {"type": "integer"}
    },
    "additionalProperties": False
}

#BOOKINGS:

bookingCreate = {
    "type": "object",
    "required": ["flight_id", "passengers"],
    "properties": {
        "flight_id": {"type": "string"},
        "passengers": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": ["full_name", "passport"],
                "properties": {
                    "full_name": {"type": "string", "minLength": 1},
                    "passport": {"type": "string", "minLength": 3},
                    "seat": {"type": ["string", "null"]}
                },
                "additionalProperties": False
            }
        }
    },
    "additionalProperties": False
}

bookingOut = {
    "type": "object",
    "required": ["id", "flight_id", "user_id", "status", "passengers"],
    "properties": {
        "id": {"type": "string"},
        "flight_id": {"type": "string"},
        "user_id": {"type": "string"},
        "status": {
            "type": "string",
            "enum": ["draft", "paid", "checked_in", "cancelled"]
        },
        "passengers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["full_name", "passport"],
                "properties": {
                    "full_name": {"type": "string"},
                    "passport": {"type": "string"},
                    "seat": {"type": ["string", "null"]}
                },
                "additionalProperties": False
            }
        }
    },
    "additionalProperties": False
}

#PAYMENTS
paymentCreate = {
    "type": "object",
    "required": ["booking_id", "amount", "payment_method"],
    "properties": {
        "booking_id": {"type": "string"},
        "amount": {"type": "number"},
        "payment_method": {"type": "string"}
    },
    "additionalProperties": False
}

paymentOut = {
    "type": "object",
    "required": ["id", "booking_id", "status"],
    "properties": {
        "id": {"type": "string"},
        "booking_id": {"type": "string"},
        "status": {
            "type": "string",
            "enum": ["pending", "success", "failed"]
        }
    },
    "additionalProperties": False
}

paymentStatus = {
    "type": "string",
    "enum": ["pending", "success", "failed"]
}