# 🤖 Proyecto Phantom - Sistema de Monitoreo de Eventos

Proyecto final del curso de Sistemas Operativos II desarrollado utilizando Docker, FastAPI, MongoDB y Ubuntu Server en la nube.

El sistema implementa una arquitectura basada en microservicios para el monitoreo y registro de eventos provenientes de un sistema robótico.

Permite:

- Registrar eventos desde un backend API
- Almacenar eventos en MongoDB
- Visualizar eventos desde una interfaz web
- Gestionar servicios mediante contenedores Docker

---

# Estructura del Proyecto

````text
proyecto-so2/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── index.html
│
├── docker-compose.yml
│
└── README.md

````
# Arquitectura del Sistema
El sistema está dividido en tres componentes principales:

# Frontend Web
Interfaz desarrollada en HTML, JavaScript y TailwindCSS que muestra el historial de eventos en tiempo real desde el navegador.

Funciones:
- Mostrar eventos registrados
- Consultar automáticamente la API
- Visualizar el estado de conexión del backend

Contenedor: `frontend_web`

Puerto utilizado: `80`

# Backend API
Servidor desarrollado en Python utilizando FastAPI.

Funciones:
- Recibir eventos mediante API REST
- Registrar eventos en MongoDB
- Procesar solicitudes del frontend
- Gestionar comandos para el sistema robótico

Endpoints principales:
````text
POST /api/events
GET /api/events
GET /leer_comando
````

Contenedor: `backend_api`
Puerto utilizado: `8001`

# Base de Datos MongoDB
Base de datos NoSQL utilizada para almacenar el historial de eventos del sistema.

Funciones:
- Persistencia de datos
- Almacenamiento de logs
- Gestión de eventos registrados

Contenedor: `mongodb_server`
Puerto utilizado: `27017`

# Tecnologías Utilizadas
- Ubuntu Server
- Docker
- Docker Compose
- FastAPI
- MongoDB
- Nginx
- HTML5
- JavaScript
- Tailwind CSS
- DigitalOcean

# Comunicación Entre Servicios
`Frontend → Backend API → MongoDB`
- El frontend consume datos desde la API REST
- El backend procesa solicitudes y registra eventos
- MongoDB almacena la información persistentemente
Todos los servicios se comunican mediante una red bridge de Docker.

# Funcionalidades
- Registro de eventos mediante API REST
- Visualización de eventos en tiempo real
- Persistencia de datos con MongoDB
- Comunicación entre microservicios
- Despliegue completo con Docker Compose
- Arquitectura desacoplada basada en contenedores
- Cómo Ejecutar el Proyecto
- Levantar contenedores

# Cómo Ejecutar el Proyecto
Levantar contenedores
`sudo docker compose up -d`
Verificar contenedores activos
`sudo docker ps`
Reiniciar servicios
`sudo docker compose down && sudo docker compose up -d`

# Integrantes del grupo
Benjamin Bonifacio Sincal Ajú Carné: 1990-23-11281
Emerson Estudardo Guzmán Vielman Carné: 1990-23-3484
Henry Daniel Cabrera Estrada Carné: 1990-23-3718

# Curso
Sistemas Operativos II
Universidad Mariano Gálvez de Guatemala
Centro Universitario de Chimaltenango
