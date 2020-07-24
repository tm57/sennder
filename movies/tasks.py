from celery.schedules import crontab
from celery.task import task
from movies.services.moviesService import MoviesService
from sennder.celery import app as celery_app


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Updates movie data every minute
    sender.add_periodic_task(crontab(), sync_data.s())


@task(name="sync movie data")
def sync_data():
    m = MoviesService()
    films = m.download_resource('films')
    m.save_movies(films)

    characters = m.download_resource('people')
    m.associate_characters_to_movies(characters)
