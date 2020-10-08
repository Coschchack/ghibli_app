from django.shortcuts import render

# Create your views here.


def movies_list_view(request):
    api_responses = ApiClient().get_concurrently((Urls.FILMS_URL.value, Urls.PEOPLE_URL.value))
    maps_collection = ApiInfoExtractor().get_people_to_movie_maps(
        all_films=api_responses[0], all_people=api_responses[1])
    context = {
        "maps_collection": Movies.objects.all()
    }
    return render(request, "movies.html", context)
