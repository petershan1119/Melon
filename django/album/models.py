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
        return f''

    def __str__(self):
        return f'{self.title} {[item for item in self.artists.all().values_list("name", flat=True)]}'
    # ', '.join([artist.name for artist in a1.artists.all()]) or ', '.join(a1.artist.values_list('name', flat=True))