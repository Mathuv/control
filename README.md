# Control
Manage pulses related to controls

## Demo

List of pulses:

http://mathuv.pythonanywhere.com/api/v1/pulses/

```json


GET /api/v1/pulses/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/vnd.api+json
Vary: Accept

{
    "links": {
        "first": "http://mathuv.pythonanywhere.com/api/v1/pulses/?page%5Bnumber%5D=1",
        "last": "http://mathuv.pythonanywhere.com/api/v1/pulses/?page%5Bnumber%5D=1",
        "next": null,
        "prev": null
    },
    "data": [
        {
            "type": "pulses",
            "id": "4c3f3462-727d-4487-b6d0-fca5bec1341e",
            "attributes": {
                "name": "My Awesome Pulse",
                "type": "Primitive",
                "maxRabiRate": 66.5,
                "polarAngle": 0.5,
                "createdAt": "2019-05-27T14:33:18.618886Z",
                "updatedAt": "2019-05-27T14:33:18.618918Z"
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 1,
            "count": 1
        }
    }
}


```

An instance of pulse:

http://mathuv.pythonanywhere.com/api/v1/pulses/4c3f3462-727d-4487-b6d0-fca5bec1341e/


```json

GET /api/v1/pulses/4c3f3462-727d-4487-b6d0-fca5bec1341e/

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/vnd.api+json
Vary: Accept

{
    "data": {
        "type": "pulses",
        "id": "4c3f3462-727d-4487-b6d0-fca5bec1341e",
        "attributes": {
            "name": "My Awesome Pulse",
            "type": "Primitive",
            "maxRabiRate": 66.5,
            "polarAngle": 0.5,
            "createdAt": "2019-05-27T14:33:18.618886Z",
            "updatedAt": "2019-05-27T14:33:18.618918Z"
        }
    }
}


```

## Model

Name: Pulse

Fields:

1. id - char, uuid field
2. name - char, max_length 100
3. type - char, max_length 20, choices of types
4. max_rabi_rate - float, with Postgres CHECK constraint >= 0 and <= 100 
5. polar_angle - float, with Postgres CHECK constraint >= 0 and <= 1
6. created_at - timestamp
7. updates_at - timestamp

Model also specifies the resource name to be in plural form

## Serializer

Name: PulseSerializer

Implements two custom validations for fields polar_angle and max_rabi_rate.

1. Validation error if 0 > max_rabi_rate > 100

```json
HTTP 400 Bad Request
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/vnd.api+json
Vary: Accept

{
    "errors": [
        {
            "detail": "Value should be between 0 and 100",
            "source": {
                "pointer": "/data/attributes/maxRabiRate"
            },
            "status": "400"
        }
    ]
}
```

2. Validation error if 0 > polar_angle > 1

```json
HTTP 400 Bad Request
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/vnd.api+json
Vary: Accept

{
    "errors": [
        {
            "detail": "Value should be between 0 and 1",
            "source": {
                "pointer": "/data/attributes/polarAngle"
            },
            "status": "400"
        }
    ]
}
```


## ViewSet

Name: PulseViewSet

Standard ModelViewSet

## To locally run the server

Requirements:
 
 Python 3.6, 
 Django, 
 Django Rest Framework, 
 Django Rest Framework JSON API, 
 Postgres
 
 
 Steps to run the server locally
 
 1. Create new database on Postgres and set following environment variables
 
     ```.env
    "NAME": os.environ.get("POSTGRES_DB", "postgres"),
    "USER": os.environ.get("POSTGRES_USER", "postgres"),
    "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
    "HOST": os.environ.get("DATABASE_URL", "postgres"),
    "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    ```
 2. Clone the git repository
 
     ```bash
     git clone https://github.com/Mathuv/control.git
     ```
 
 3. Create python virtual environment with python 3.6
 
     ```bash
    cd control
    python -m venv .env
    ```

 4. Activate the virtual environment and install the python requirements
     ```bash
    source .env/bin/activate
    pip install -r requirements.txt

    ```

5. Performa database migration (make sure the environment variables related to db connection are set)
    ```bash
    ./manage.py migrate
    ```

6. Run the django development server
    ```bash
    ./manage.py runserver
    ```

You can access the REST API under
http://localhost:8000/api/v1/pulses/

## Work in Progress

1. Upload pulses in CSV format
2. Download pulses in CSV format

## TODO

1. Upload pulses in CSV format
2. Download pulses in CSV format
3. Handle CSV Uplaod with celery workers (asynchronous handling)
4. Implement unit tests
5. Set up CI/CD pipeline (candidates: Travis CI + Heroku)
6. Swagger based API Documentation

