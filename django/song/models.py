from django.db import models

from album.models import Album
from artist.models import Artist


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist, through='ArtistSong')
    # artist = models.ManyToManyField(Artist, through='ArtistSong', related_name='song')

    def __str__(self):
        return self.title


class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='relation_artist')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='relation_song')
    # album = models.ForeignKey(Album, on_delete=models.CASCADE)
    demo_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'artist: {self.artist} - song: {self.song.title}'