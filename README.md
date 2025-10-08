# ✈️ Airline API Automation Framework

Framework de automatización de pruebas para una API de aerolínea.
Desarrollado en **Python + Pytest**, con enfoque modular y helpers reutilizables.

---

## 📦 Estructura del proyecto

```
AirlineDemoApiTest/
├─ .github/
│  └─ workflows/
│     └─ test-suite-airline.yml
├─ .env
├─ requirements.txt
├─ README.md
├─ utils/
│  ├─ api_helpers.py          # api_request(), manejo BASE_URL, logging, retries opcional
│  ├─ settings.py             # BASE_URL y endpoints: FLIGHTS, BOOKINGS, USERS, AIRCRAFTS...
│  ├─ schemas.py              # esquemas/validaciones (si usas pydantic o jsonschema)
│  ├─ support/                # data builders / generadores / recursos auxiliares
│  │  ├─ __init__.py
│  │  ├─ users.py             # create_user(), helpers de usuario
│  │  ├─ aircrafts.py         # ensure_aircraft_id(), helpers de aircraft
│  │  └─ data_builders.py     # generadores random (passport, seat, fechas, etc.)
│  └─ services/               # “clientes” de dominio para la API
│     ├─ __init__.py
│     ├─ flights.py           # create_flight(), get_flight(), update_flight(), delete_flight()
│     └─ bookings.py          # create_booking(), get_booking(), delete_booking()
├─ tests/
│  ├─ conftest.py             # aquí viven las fixtures (auth_headers, etc.)
│  ├─ api/
│  │  ├─ test_flights_positive_scenarios.py
│  │  └─ test_flights_negative_scenarios.py
│  ├─ e2e/
│  │  └─ test_e2e_book_flight.py   # snake_case
│  └─ features/                # (solo si SÍ usarás BDD en este repo)
│     └─ __init__.py
└─ .gitignore                  # incluye .env, .venv, __pycache__/, .pytest_cache/
```

---

## 🚀 Flujo E2E principal

1. Crear **usuario pasajero**
2. Crear **vuelo** (con aircraft asociado)
3. Crear **booking** enlazando el usuario y vuelo
4. Consultar booking y validar datos
5. Eliminar booking
6. Eliminar vuelo

Archivo de prueba:
`tests/e2e/test_booking_flow_simple.py`

---

## ⚙️ Requisitos

* Python ≥ 3.10
* Virtualenv o venv activo
* Librerías principales:

  ```
  pip install requests pytest faker
  ```

---

## 🧠 Ejecución de pruebas

Para correr todas las pruebas:

```bash
pytest -v
```

Para correr solo las pruebas E2E:

```bash
pytest tests/e2e -v
```

---

## 🧉 Helpers principales

| Módulo           | Descripción                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| `flights.py`     | Crea, obtiene, actualiza y elimina vuelos                               |
| `bookings.py`    | Maneja reservas, incluyendo creación automática de usuario/vuelo        |
| `support.py`     | Recursos auxiliares (crear usuario, crear aircraft)                     |
| `api_helpers.py` | Función base para llamadas HTTP (maneja headers, BASE_URL, status)      |
| `settings.py`    | Contiene constantes de endpoints (`FLIGHTS`, `BOOKINGS`, `USERS`, etc.) |

---

## 🔍 Validaciones comunes

* Status codes esperados: 200, 201, 204
* IDs de vuelo, usuario y booking válidos
* Campos mínimos en responses (`id`, `flight_id`, `user_id`, `passengers`)
* Limpieza final (DELETE ejecutado con éxito)

