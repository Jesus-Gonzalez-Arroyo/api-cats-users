# 🐱 Cat & User API (FastAPI + MongoDB + Docker)

Este proyecto expone una API RESTful con FastAPI y MongoDB para consultar razas de gatos (usando [TheCatAPI](https://thecatapi.com)) y gestionar usuarios.

---

## 🚀 Ejecutar con Docker

### 1. Requisitos

- Docker
- Docker Compose

### 2. Levantar el proyecto

```bash
docker-compose up --build
```

Esto levantará:

- FastAPI en [http://localhost:8000](http://localhost:8000)
- Swagger UI en [http://localhost:8000/docs](http://localhost:8000/docs) (Para hacer pruebas)
- MongoDB en el puerto 27017

## 📦 Endpoints disponibles

### 🐱 Rutas de Gatos (`/breeds`)

| Método | Endpoint                  | Descripción                              |
|--------|---------------------------|------------------------------------------|
| GET    | `/breeds/`                | Lista todas las razas de gatos           |
| GET    | `/breeds/{breeds_id}`      | Detalles de una raza por ID              |
| GET    | `/breeds/search?name=...`    | Buscar razas por nombre                  |

---

### 👤 Rutas de Usuario (`/user`)

| Método | Endpoint             | Descripción                              |
|--------|----------------------|------------------------------------------|
| GET    | `/user/`             | Lista todos los usuarios                 |
| POST   | `/user/`             | Crea un usuario (username generado)      |
| POST    | `/user/login`        | Login del usuario (envía JSON en body)   |

---

## 🧪 Pruebas

Puedes probar con herramientas como:

- Postman
- Navegador (Swagger UI)

---

## 📁 Estructura del Proyecto

```
├── app/
│   ├── api/routes/         # Rutas de la API
│   ├── controllers/        # Lógica de control
│   ├── services/           # Servicios externos
│   ├── repository/         # Acceso a la base de datos
│   ├── models/             # Modelos internos
│   ├── schemas/            # Esquemas Pydantic
│   ├── utils/              # Utilidades
│   ├── tests/              # Pruebas unitarias
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
```

## ✅ Verificar test

Para correr los test unitarios y ver el buen funcionamiento de la api ejecutar (siempre con el servidor activo)
```
pytest app/tests/test_cats.py
pytest app/tests/test_users.py
```