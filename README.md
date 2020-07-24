Please make sure docker is installed on your machine.

In the first terminal run `docker-compose up`
In the second terminal run `docker exec -it movies-api python manage.py migrate`
In the third terminal run `docker exec -it  movies-api celery -A sennder beat --pidfile=/opt/celeryd.pid`
and in the 4th, run `docker exec -it movies-api celery -A sennder worker -l info`

Then visit http://localhost:8080/movies


