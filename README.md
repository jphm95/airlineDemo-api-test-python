# ✈️ Airline API Automation Framework

Framework de automatización de pruebas para una API de aerolínea.
Desarrollado en **Python + Pytest**, con enfoque modular y helpers reutilizables.

---

## 📦 Estructura del proyecto

```
utils/
 ├── api_helpers.py      # Función genérica api_request()
 ├── settings.py         # Rutas base (BASE_URL, ENDPOINTS)
 ├── flights.py          # CRUD de vuelos
 ├── bookings.py         # CRUD de reservas (bookings)
 ├── support.py          # Recursos auxiliares: crear usuarios, aircrafts
 └── fixtures.py         # Fixtures de autenticación y setup global
tests/
 ├── api/                # Pruebas unitarias o de endpoint
 ├── e2e/                # Escenarios integrados (flujo completo)
 └── conftest.py         # Configuración Pytest
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

