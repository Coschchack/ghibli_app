from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100)


class Person(models.Model):
    name = models.CharField(max_length=100)
    # movie_id = models.ForeignKey("Movie", on_delete=)
    movies = models.ManyToManyField("Movie", related_name="persons")
