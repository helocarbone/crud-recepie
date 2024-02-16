# crud-recepie

## Usage Commands
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

* Create superuser
> docker-compose run --rm app sh -c "python manage.py createsuperuser"


## APIs Checking
A swagger is running in http://127.0.0.1:8000/api/docs you can use it to play around
