# Calculus
Calculus is a work in progress API that receives parameters and returns responses.

## Installation
```bash
git clone git@github.com:dayvidwhy/calculus.git
cd calculus
docker-compose up -d
```

You can then start making requests to port 5000 on your local machine and they are passed through to the docker container.

## Development
You can use docker compose to start up the development environment.

Changes made to `app.py` will be available from `localhost:5000` being passed through from the container.

Docker is used as a repeatable development environment and saves installing python dependencies locally or using something like python environment manager.

## Deployment
THe docker container can be built for deployment.
