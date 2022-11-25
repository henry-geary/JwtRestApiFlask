### Challenge de ingreso Infra y Endpoint Security
Desafio principal: Python Redis Docker Tests

### Para iniciar el proyecto:

Crear archivo .env (usar de referencia el archivo .env.example)
    
    El secret puede ser cualquier palabra, mientras que el
    admin es el nombre con el que vas a tener que loguearte
    en el endpoint '/api/login'
    
En la terminal:
```docker
    docker compose build
    
    docker compose up
```



#### Librerias usadas:
* Flask
* pyjwt
* python-dotenv
* redis
* requests

#### Tests: 
* pytest
* pytest-redis
* pytest-mock
* pytest-flask
* fakeredis


#### [Link al repo en  Github](https://github.com/henry-geary/JwtRestApiFlask)
<hr/>

#### Dentro de <strong>./Utils/resourses</strong> se encuentra la coleccion de POSTMAN 

<hr/>

### Endpoints

### `Endpoint 001`: 
#### Autenticarse como Admin para poder acceder a los demas endpoints

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
    "msg": "hi! i am a message"
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

## Tests

### Tests unitarios
    Los tests unitarios no requieren coneccion a internet,
    o estar corriendo el docker.
    Se dividen en 2, uno sobre la funcionalidad del service.
    Y el otro sobre las respuestas de los endpoints de Api.
    

### Test de integracion
    Requiere que el proyecto este corriendo en docker.
    





Puerto para entrar en redis-commander: http://localhost:8081/ 

[Graficas e Historial de pushs](https://www.cybertalk.org/2022/03/03/youve-been-phished-what-to-do-next/)

[Como parar y/o remover contendores](https://www.ibm.com/docs/en/connect-direct/6.1.0?topic=container-stoprestart-procedure)