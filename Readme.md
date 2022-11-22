### Challenge de ingreso Python

#### Librerias usadas:
* Flask
* pyjwt
* python-dotenv
* redis
* pytest
* poetry

#### Tests: 
* unittest


#### [Link al repo en  Github](https://github.com/henry-geary/JwtRestApiFlask)
<hr/>

#### Dentro de ./resourses se encuentra la coleccion de POSTMAN 

## Levantar el proyecto

* En terminal correr la siguiente linea de código.
```
   docker compose up
```

<hr/>

### Endpoints

### `Endpoint 001`: 
#### Autenticarse como Admin para poder acceder a los demas endpoints (token expired date: 48hs)

### Sign:


| Method   | SIGN                             |
|----------|----------------------------------|
| POST     | `/api/login`                     |
| Request  | Body (JSON)                      |
| Response | Status Code 200 (todo OK)        |
| Response | Status Code 400 (Bad Request)    |
| Response | Status Code 404 (User Not Found) |
Request:
```json
{
    "username": "jefecito"
}
```
| Parámetros   | Tipo | Descripción/Ejemplo              |
|--------------|------|----------------------------------|
| username     | str  | Nombre del usuario administrador |

Payload:
```json
{
    "Status": "Successfully Auth",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImplZmVjaXRvIiwiZXhwIjoxNjY4NzczMzY0fQ.kbsCYPHvcz32q1DTEOrbx2eZQknzlxu0NE4qvKemwjs"
}

```
<hr/>

### `Endpoint 002`:
#### Revisa el estado de salud del servidor de Redis (Bearer JWT Auth Required)

### Sign:   


| Method   | SIGN                           |
|----------|--------------------------------|
| GET      | `api/queue/ping_redis`         |
| Response | Status Code 200 (todo OK)      |
| Response | Status Code 500 (Server Error) |

Payload:
```json
{
    "Connection": "OK"
}
```
<hr/>

### `Endpoint 003`:
#### Pushea un mensaje a la Queue en Redis (Bearer JWT Auth Required)

### Sign:


| Method   | SIGN                          |
|----------|-------------------------------|
| POST     | `/api/queue/push`             |
| Request  | Body (JSON)                   |
| Response | Status Code 200 (todo OK)     |
| Response | Status Code 400 (Bad Request) |
Request:
```json
{
    "msg": "chau"
}
```
| Parámetros   | Tipo | Descripción/Ejemplo       |
|--------------|------|---------------------------|
| msg     | str  | Contentido del mensaje    | 

Payload:
```json
{
  "status": "ok"
}
```
<hr/>

### `Endpoint 004`:
#### Elimina y retorna el proximo mensaje de la Queue (Bearer JWT Auth Required)

### Sign:   


| Method   | SIGN                           |
|----------|--------------------------------|
| GET      | `api/queue/ping_redis`         |
| Response | Status Code 200 (todo OK)      |
| Response | Status Code 400 (Bad Request)  |
| Response | Status Code 500 (Server Error) |

Payload:
```json
{
  "status": "ok",
  "message": <msg>
}
```
<hr/>

### `Endpoint 005`:
#### Retorna la cantidad de mensajes en Queue (Bearer JWT Auth Required)

### Sign:   


| Method   | SIGN                           |
|----------|--------------------------------|
| GET      | `api/queue/ping_redis`         |
| Response | Status Code 200 (todo OK)      |
| Response | Status Code 400 (Bad Request)  |
| Response | Status Code 500 (Server Error) |

Payload:
```json
{
  "status": "ok",
  "count": <count>
}
```
### Fin Endpoints

<hr/>




```
docker pull redis

docker run -d --name miredis -p 6379:6379 redis

docker pull rediscommander/redis-commander

docker run --rm --name rd -d --env REDIS_HOSTS=local:host.docker.internal:6379 -p 8081:8081 rediscommander/redis-commander:latest  

```



Puerto para entrar en redis-commander: http://localhost:8081/ 

[Graficas e Historial de pushs](https://www.cybertalk.org/2022/03/03/youve-been-phished-what-to-do-next/)

[Como parar y/o remover contendores](https://www.ibm.com/docs/en/connect-direct/6.1.0?topic=container-stoprestart-procedure)