# Sistema de Scrapping de produtos em Django

## Descrição
Sistema para varrer o site [Open Food Facts](https://world.openfoodfacts.org/) extrair os produtos, 
salvar numa base de dados e disponibilizar via postman

## Stacks usadas:
- Django
- Django Rest Framework (API)
- Docker (Contendo todos os recursos para funcionar) 
- Postgres
- Celery (Worker para lidar com a task)
- Celery beat (cronjob para disparar a task a cada x minutes)
- Redis
- Hooks de pré-commits (organização de código)
- Para o sistema de alertas, eu criei um model de alerta para armazenar os erros quando cair em uma exessão

## Passo a passo:
- Baixe o código
- Renomeie o .env-exemplo para .env
- Atualize a variável: `CRONTAB_TIME` para a data e hora desejados
- Apenas ```docker-compose up --build``` e esperar o build finalizar!

Uma vez que o docker esteja rodando, não deve ter problemas com a aplicação
- Para testar o endpoint `GET /`, execute um cUrl ou via postman: `http://127.0.0.1:8000/`  
- Para testar o endpoint `GET /products`, execute um cUrl ou via postman: `http://127.0.0.1:8000/products`
- Para testar o endpoint `GET /products/id`, execute um cUrl ou via postman: `http://127.0.0.1:8000/products/<id>`

- Para ver o swagger use o endpoint `http://127.0.0.1:8000/swagger`
- Para ver a documentação do projeto use o endpoint `http://127.0.0.1:8000/redoc`


### Contas de usuário:
Conta administradora:
```
username: admin
senha: admin
```
para acessar vá até `http://127.0.0.1:8000/admin`
Fique à vontade para criar mais contas e testar a sua maneira.

## Testes com APITestCase
Só rodar dentro do docker:
```docker-compose run api bash```
then:
```python manage.py test```

>This is a challenge by Coodesh