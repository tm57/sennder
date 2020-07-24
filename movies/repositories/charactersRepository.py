from movies.models.character import Character
from movies.models.movie import Movie
from movies.repositories.repository import Repository


class CharactersRepository(Repository):
    def save(self, models):
        result = []
        for model in models:
            movie = Movie.objects.filter(id=model.get("uuid")).first()
            if movie:
                result.append(Character.objects.get_or_create(**model))

        return result
