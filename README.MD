# Api Logs

## Run
    Na raiz do projeto
        $ sudo docker-compose up (para sistemas operacionais linux/debian)

## Swagger
    localhost:8000/api/swagger/


### Infos
    - Api foi desenvolvida em ambiente linux - Ubuntu 20.04
    - Api foi testada utilizando Postman


## Step by step
    Passo 1: popular o banco
    Passo 2: gerar CSV base para cálculos
    Passo 3: gerar os relatórios em CSV solicitados no teste (os mesmos são gerados na raiz do projeto)
    Passo 4: rodar os testes e análise de cobertura



### Teste Endpoints
    - Para popular o banco, fazer 'get' no enpoint: localhost:8000/api/api/db/populate/
    - Para gerar arquivo CSV base para cálculos solicitados no teste, fazer get no endpoint: localhost:8000/api/to/csv/
    - Para gerar relatório de Requisições por consumidor, fazer 'get' no enpoint: localhost:8000/api/api/requests/consumer/
    - Para gerar relatório de Requisições por serviço, fazer 'get' no enpoint: localhost:8000/api/api/requests/service/
    - Para gerar relatório de Tempo médio de request , proxy e gateway por serviço, fazer 'get' no enpoint: localhost:8000/api/api/average/time/
    - Para visualizar os logs(.txt) no banco fazer 'get' no enpoint: localhost:8000/api/workdata/

### Tests and Coverage
     Na raiz do projeto
        $ coverage run manage.py test
        $ coverage report
