
# Moxie API

This is the Moxie API project. It is a Django-based application that can be easily started and managed using Docker Compose. Below are the instructions on how to set up the project, run it with Docker Compose, and make some basic API calls.

## Requirements

Before starting, ensure that you have the following installed on your machine:

- Docker
- Docker Compose

## Setup Instructions

### Clone the repository:

```bash
git clone https://github.com/your-username/moxie-api.git
cd moxie-api
```

### Create a `.env` file:

Create a `.env` file at the root of your project and add the necessary environment variables:

```bash
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_NAME=mydb
DJANGO_PORT=8000
```

These values will be used for setting up the PostgreSQL database and the Django app.

### Run Docker Compose:

Now that everything is set up, you can start the project using the following command:

```bash
docker compose up --build
```

This will:

- Build the Docker images for your services.
- Start the PostgreSQL database.
- Start the Django web application.

### Create the Database:

After the containers are up and running, open a new terminal and run the following command to apply the migrations and create the initial database structure:

```bash
docker compose exec web python manage.py migrate
```

### Create a Superuser (Optional):

If you need access to the Django admin, create a superuser by running the following command:

```bash
docker compose exec web python manage.py createsuperuser
```

## Access the Application:

- The Django app will be running at [http://localhost:8000](http://localhost:8000) (or the port you specified in your `.env` file as `DJANGO_PORT`).
- The Django admin will be available at [http://localhost:8000/admin](http://localhost:8000/admin).

## API Usage

Below are some example API calls you can make to interact with the application.

### 1. List Services

Get the list of all services:

```bash
curl -X GET http://localhost:8000/api/services/ -H "Authorization: Bearer <your_token>"
```

### 2. Create a New Service

Create a new service for a MedSpa:

```bash
curl -X POST http://localhost:8000/api/services/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your_token>" \
-d '{
    "name": "Facial Treatment",
    "description": "A relaxing facial service",
    "price": "100.00",
    "duration": "01:00:00",
    "medspa": 1
}'
```

### 3. Create a New Appointment

Create a new appointment and associate it with multiple services:

```bash
curl -X POST http://localhost:8000/api/appointments/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your_token>" \
-d '{
    "medspa": 1,
    "services": [1, 2],
    "start_time": "2024-10-10T15:00:00Z",
    "status": "scheduled"
}'
```

### 4. Get Appointment Details

Get details of an existing appointment, including the total price and duration:

```bash
curl -X GET http://localhost:8000/api/appointments/1/ -H "Authorization: Bearer <your_token>"
```

### 5. List MedSpas

Get the list of all MedSpas:

```bash
curl -X GET http://localhost:8000/api/medspas/ -H "Authorization: Bearer <your_token>"
```

### 6. Authentication

The API uses token-based authentication. To get a token, you can use the following endpoint:

```bash
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{
    "username": "your_username",
    "password": "your_password"
}'
```

The response will include an access token that you can use in the Authorization header for subsequent API requests.

## Stopping the Project

To stop the running containers, press `CTRL + C` in the terminal where `docker compose up` is running, or use the following command:

```bash
docker compose down
```
