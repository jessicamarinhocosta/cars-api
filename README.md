# Cars API

REST API desenvolvida em *Python*, utilizando o web framework *Flask*.

## Executando a APP

Criar ambiente à partir do Docker Compose:

```
docker-compose up -d 
```

## Operações

##### /GET

```
curl --location --request GET 'http://127.0.0.1:5000/cars' \
--header 'Content-Type: application/json' \
--data-raw '{
    "cor": "branco",
    "placa": "OXO-2021",
    "ano": "2020",
    "modelo": "golf"
}'
```

##### /POST

```
curl --location --request POST 'http://127.0.0.1:5000/cars' \
--header 'Content-Type: application/json' \
--data-raw '{
    "cor": "branco",
    "placa": "OXO-2021",
    "ano": "2020",
    "modelo": "golf"
}'
```

##### /DELETE

```
curl --location --request DELETE 'http://127.0.0.1:5000/cars' \
--header 'Content-Type: application/json' \
--data-raw '{
    "cor": "branco",
    "placa": "OXO-2021",
    "ano": "2020",
    "modelo": "golf"
}'
```

##### /PUT

```
curl --location --request PUT 'http://127.0.0.1:5000/cars' \
--header 'Content-Type: application/json' \
--data-raw '{
    "cor": "vermelho",
    "placa": "OXO-2021",
    "ano": "2017",
    "modelo": "uno"
}'
```
