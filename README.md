# GeTA Backend

## steps to run server

1. first you need `.env` file in `./software_design_backend/` with following fields:
    `SECRET_KEY`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`


2. run following commands to run docker and migrate database
```
docker-compose build
docker-compose up
docker-compose exec geta-backend python manage.py migrate
```
