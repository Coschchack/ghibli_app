from django.shortcuts import render
from django.views.decorators.cache import cache_page

from ghibli_api.enums import Urls
from ghibli_api.api_client import ApiClient
from ghibli_api.api_info_extractor import ApiInfoExtractor

# Create your views here.


@cache_page(60)
def movies_list_view(request):
    api_responses = ApiClient().get_concurrently((Urls.FILMS_URL.value, Urls.PEOPLE_URL.value))
    maps_collection = ApiInfoExtractor().get_people_to_movie_maps(
        all_films=api_responses[0], all_people=api_responses[1])
    context = {
        "maps_collection": maps_collection
    }
    return render(request, "movies.html", context)
