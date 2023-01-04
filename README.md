# GeTA Backend

## run server

- first you need `.env` file in `./software_design_backend/` with following fields:
    `SECRET_KEY`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`

  
- run following commands to start project for development

    ```
    docker-compose build
    docker-compose up
    docker-compose exec geta-backend python manage.py migrate
    ```

- run following commands to start project for production

    ```
    docker-compose -f docker-compose-prod.yml build
    docker-compose -f docker-compose-prod.yml up
    docker-compose -f docker-compose-prod.yml exec geta-backend python manage.py migrate
    docker-compose -f docker-compose-prod.yml exec geta-backend python manage.py collectstatic
    ```
