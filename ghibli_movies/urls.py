from django.urls import path

from ghibli_movies.views import movies_list_view


urlpatterns = [
    path("", movies_list_view, name="movies_list"),
]
