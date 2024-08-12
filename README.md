## Description:

This system is intended for downloading user metrics to the PostgreSQL database.

## Run:

1. Make sure you have Docker and docker-compose installed.
2. Make sure that your port 5432 is not occupied by another process
3. Clone the repository and go to its directory.
4. Start the containers.

 ```bash
 docker-compose up --build:
 ```
5. The database will be available on port 5432.

## Database schema:

- `user_metrics`. stores user metrics.

## Settings:

- The PostgreSQL database is configured with the name `metrics_db', the user `postgres' and the password `testpassword1234'.

## Expansion:

- To add new metrics or fields, update the SQL script and application (app.py).