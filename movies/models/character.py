from django.db import models

from movies.models.movie import Movie


class Character(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=1000)  # using the api id as a unique id for characters here
    name = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'movies'
        constraints = [
            models.UniqueConstraint(fields=['movie_id', 'uuid'], name='u_movie_id_uuid')
        ]
