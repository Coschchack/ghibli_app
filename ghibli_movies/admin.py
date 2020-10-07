from django.contrib import admin

from ghibli_movies.models import Movie, Person


admin.site.register(Movie)
admin.site.register(Person)
