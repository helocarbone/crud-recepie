# crud-recepie

## Dockerfile
* Start
> docker-compose build
* Drop
> docker-compose down

* Run lint
> docker-compose run --rm app sh -c "flake8"

* Run server
> docker-compose up

* Run tests
>  docker-compose run --rm app sh -c "python manage.py test"


____

## Usage

* Create superuser
> docker-compose run --rm app sh -c "python manage.py createsuperuser"
