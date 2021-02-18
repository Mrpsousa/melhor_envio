# Api Logs

## Run
    Na raiz do projeto
        $ sudo docker-compose up
        $ python3 manage.py makemigrations
        $ python3 manage.py migrate
        $ python3 manage.py runserver 

## Swagger
    http://127.0.0.1:8000/api/swagger/


## Tests and Coverage
     Na raiz do projeto
        $ coverage run manage.py test
        $ coverage report

### DB Populate
    - Para popular o banco, fazer requisição 'get' no enpoint: http://127.0.0.1:8000/api/db/populate/