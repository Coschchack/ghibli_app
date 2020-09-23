import threading

from celery.decorators import periodic_task

from ghibli_movies.models import Movies
from ghibli_api.api_client import ApiClient
from ghibli_api.api_info_extractor import ApiInfoExtractor


@periodic_task(run_every=60, name="update_movies")
def update_movies():
    # all_films = ApiClient.get_all_films_response().json()
    # all_people = ApiClient.get_all_people_response().json()
    films_thread = threading.Thread(target=ApiClient.get_all_films_response, name="films_thread")
    people_thread = threading.Thread(target=ApiClient.get_all_people_response, name="people_thread")
    # start get api response in threads
    films_thread.start()
    people_thread.start()
    # wait for threads to finish before proceeding
    films_thread.join()
    people_thread.join()
    maps_collection = ApiInfoExtractor().get_people_to_movie_maps(all_films=all_films, all_people=all_people)
    Movies.objects.all().delete()
    for map_ in maps_collection:
        Movies.objects.create(movie_title=map_.movie_title, people=map_.people)
