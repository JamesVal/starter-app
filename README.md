# starter-app
Starter App for Django with Basic Functionality

## Setup Application

Create a `.env` file inside of the `server` directory. The following will have to be added provided:

```
DEFAULT_USER=
DEFAULT_PASSWORD=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=
```

### Running with Docker

To run the app, `cd` into the `server` directory and run `docker-compose up`. If successful, you should be able to navigate to `localhost:8000/admin` and log into the Django Admin using your `DEFAULT_USER` and `DEFAULT_PASSWORD`

### Running with Virtual Environment

The application can be run with a virtual environment with the database running separately.
