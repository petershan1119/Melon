from django.db import models

from artist.models import Artist


# class Album(models.Model):
#     title = models.CharField(max_length=255)
#     artist = models.ManyToManyField(Artist)
#
#     def __str__(self):
#         return self.title


class Album(models.Model):
    title = models.CharField('앨범명', max_length=100)
    img_cover = models.ImageField('커버 이미지', upload_to='album', blank=True)
    artists = models.ManyToManyField(Artist, verbose_name='아티스트 목록')
    release_date = models.DateField()
    # genre = models.CharField(max_length=100)

    @property
    def genre(self):
        return ', '.join(self.song_set.values_list('genre', flat=True).distinct())

    def __str__(self):
        return '{title} [{artist}]'.format(
            title=self.title,
            artist=', '.join(self.artists.values_list('name', flat=True))
        )
        # return f'{self.title} {[item for item in self.artists.all().values_list("name", flat=True)]}'
    # ', '.join([artist.name for artist in a1.artists.all()]) or ', '.join(a1.artists.values_list('name', flat=True))