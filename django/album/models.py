from django.db import models

from artist.models import Artist


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        return self.title