from django.shortcuts import render

from movies.services.moviesService import MoviesService


def movies(request):
    movies_service = MoviesService()


    m = MoviesService()
    films = m.download_resource('films')
    m.save_movies(films)

    characters = m.download_resource('people')
    print(characters)
    m.associate_characters_to_movies(characters)
    context = {
        'movies': movies_service.get_saved_movies()
    }

    return render(request, 'movies/index.html', context)
