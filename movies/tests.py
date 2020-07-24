from django.test import TestCase

from movies.models.character import Character
from movies.models.movie import Movie
from movies.services.moviesService import MoviesService
from django.conf import settings


class MoviesServiceTest(TestCase):
    def setUp(self):
        self.api_movies = [
            {
                "id": '1',
                "title": "Chronicles of Narnia 1"
            },
            {
                "id": '2',
                "title": "Chronicles of Narnia 2"
            },
            {
                "id": '3',
                "title": "Chronicles of Narnia 3"
            },
        ]
        url = settings.MOVIES_API_ENDPOINT + 'films'

        self.movie_characters = [
            {
                'id': '1',
                'name': 'Polly',
                'films': [url + '1']
            },
            {
                'id': '2',
                'name': 'Digory',
                'films': [url + '1', url + '2']
            },
            {
                'id': '3',
                'name': 'Edmond',
                'films': [url + '1', url + '2', url + '3']
            },
            {
                'id': '30',
                'name': 'The white witch',
                'films': [url + '1', url + '2']
            }

        ]

    def test_movies_saved_correctly(self):
        m = MoviesService()
        saved = m.get_saved_movies()
        self.assertEquals([], saved)
        m.save_movies(self.api_movies)

        saved = m.get_saved_movies()
        self.assertEquals(3, len(saved), '3 movies are saved')
        for movie in saved:
            self.assertIsNotNone(movie.id)
            self.assertIsNotNone(movie.title)

    def test_associate_movie_to_character(self):
        m = MoviesService()
        saved = list(Character.objects.all())
        self.assertEquals([], saved)

        # Let's create the movies first
        m.save_movies(self.api_movies)
        # then do the association
        m.associate_characters_to_movies(self.movie_characters)

        movies_with_characters = m.get_saved_movies()
        for movie in movies_with_characters:
            print(movie.title)
            characters = movie.character_set.all()
            for character in characters:
                print("     " + character.name)
                self.assertEquals(movie.id, character.movie_id)
