from celery.decorators import periodic_task

from ghibli_movies.models import Movies
from ghibli_api.api_client import ApiClient
from ghibli_api.enums import Urls
from ghibli_api.api_info_extractor import ApiInfoExtractor


@periodic_task(run_every=60, name="update_movies")
def update_movies():
    api_responses = ApiClient().get_concurrently((Urls.FILMS_URL.value, Urls.PEOPLE_URL.value))
    maps_collection = ApiInfoExtractor().get_people_to_movie_maps(
        all_films=api_responses[0], all_people=api_responses[1])
    Movies.objects.all().delete()
    for map_ in maps_collection:
        Movies.objects.create(movie_title=map_.movie_title, people=map_.people)
