from django.shortcuts import render

from urllib.parse import urlparse

from ghibli_movies.models import Movie, Person
from ghibli_api.api_client import ApiClient
from ghibli_api.enums import Urls


# Create your views here.


def movies_list_view(request):
    api_responses = ApiClient().get_concurrently((Urls.FILMS_URL.value, Urls.PEOPLE_URL.value))
    Movie.objects.all().delete()
    Person.objects.all().delete()
    for movie in api_responses[0]:
        Movie.objects.create(source_film_id=movie["id"], title=movie["title"])
    for person in api_responses[1]:
        for person_film in person["films"]:
            film_id = str(urlparse(person_film).path).rsplit("/")[-1]
            Person.objects.create(name=person["name"], source_film_id=film_id)
    context = {
        "movies": Movie.objects.all(),
        "people": Person.objects.all(),
    }
    return render(request, "movies.html", context)


# movie1 = Movie.objects.create(source_film_id=movie["id"], title=movie["title"])
# person1 = Person.objects.create(name=person["name"], source_film_id=film_id)
# movie1.perons.add(person1)
