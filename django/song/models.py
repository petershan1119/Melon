from django.db import models

from album.models import Album
from artist.models import Artist


# class Song(models.Model):
#     title = models.CharField(max_length=255)
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     artist = models.ManyToManyField(Artist, through='ArtistSong')
#     # artist = models.ManyToManyField(Artist, through='ArtistSong', related_name='song')
#
#     def __str__(self):
#         return self.title
#
#
# class ArtistSong(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='relation_artist')
#     song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='relation_song')
#     # album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     demo_date = models.DateTimeField(null=True)
#
#     def __str__(self):
#         return f'artist: {self.artist} - song: {self.song.title}'


class Song(models.Model):
    album = models.ForeignKey(Album,
                              verbose_name='앨범',
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
    )
    title = models.CharField('곡 제목', max_length=100)
    genre = models.CharField('장르', max_length=100)
    lyrics = models.TextField('가사', blank=True)
    artist = models.ManyToManyField(Artist, through='ArtistSong')

    @property
    def artists(self):
        # result = self.album.artists.values_list('name', flat=True)
        return self.album.artists.all()

    @property
    def release_date(self):
        return self.album.release_date

    @property
    def formatted_release_date(self):
        return self.release_date.strftime('%Y-%m-%d')

    def __str__(self):
        artists = ', '.join(self.album.artists.all().values_list('name', flat=True))
        return f'{artists} - {self.title} ({self.album.title})'


class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='relation_artist')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='relation_song')
    # album = models.ForeignKey(Album, on_delete=models.CASCADE)
    demo_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'artist: {self.artist} - song: {self.song.title}'