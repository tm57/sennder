from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    id = models.CharField(primary_key=True, max_length=1000)

    class Meta:
        app_label = 'movies'
