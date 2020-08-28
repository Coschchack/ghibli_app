from django.shortcuts import render

from ghibli_movies.models import Movies

# Create your views here.


def movies_list_view(request):
    context = {
        "maps_collection": Movies.objects.all()
    }
    return render(request, "movies.html", context)
