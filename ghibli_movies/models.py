from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_title = models.TextField()
    people = models.TextField()
