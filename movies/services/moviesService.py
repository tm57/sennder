from movies.models.character import Character
from movies.models.movie import Movie
from movies.repositories.charactersRepository import CharactersRepository
from movies.repositories.moviesRepository import MoviesRepository
from django.conf import settings

import requests


class MoviesService:
    def __init__(self):
        self.movies_repository = MoviesRepository(Movie)
        self.characters_repository = CharactersRepository(Character)

    def get_saved_movies(self):
        return self.movies_repository.get()

    def save_movies(self, api_movies):
        movies_to_save = []
        for movie in api_movies:
            new_movie = {
                "id": movie["id"],
                "title": movie["title"]
            }
            movies_to_save.append(new_movie)

        if movies_to_save:
            self.movies_repository.save(movies_to_save)

    def associate_characters_to_movies(self, characters):
        to_save = []
        for character in characters:
            movies = character["films"]
            for movie in movies:
                offset_length = 37
                movie_id = movie[offset_length:]
                new_entry = {
                    "uuid": character["id"],
                    "name": character["name"],
                    "movie_id": movie_id
                }
                to_save.append(new_entry)

        self.characters_repository.save(to_save)
        return characters

    @staticmethod
    def download_resource(resource_name):
        if resource_name not in ['films', 'people']:
            raise Exception('only one of `films` or `people` is accepted as resource name')

        movies_api_endpoint = settings.MOVIES_API_ENDPOINT

        response = requests.get(movies_api_endpoint + resource_name)
        return response.json()
