# FastAPI-Postgres-Docker

This project sets up a Dockerized environment for a FastAPI application, PostgreSQL database, and NGINX as a reverse proxy. It allows you to quickly deploy and run a FastAPI application with PostgreSQL as the backend, all managed through Docker Compose.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sudan94/fastapi-postgres-docker-template.git
   cd fastapi-postgres-docker
    ```
2. Update the .env file with your database credentials:
    ```js
    POSTGRES_USER=your_username
    POSTGRES_PASSWORD=your_password
    POSTGRES_SERVER=your_postgres_servername
    POSTGRES_PORT=your_postgres_running_port
    POSTGRES_DB=your_database
    ```
3. Build and run the Docker containers:

    ```bash
    docker-compose up -d
    ```

### Usage
After running ```docker-compose up -d```, your FastAPI application will be accessible via NGINX at http://localhost:8080/fastapi/docs.

---
Enjoy building with FastAPI, PostgreSQL, and Docker! If you have any questions or run into issues, feel free to open an issue in the repository.

