from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    picture = models.ImageField(upload_to='artist_images', blank=True, null=True)  # Permite nulo y blanco

    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=30, null=False)
    release_year = models.IntegerField(null=False)
    genre = models.CharField(max_length=30, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='album_images', default='default_album_image.jpg')  # Valor por defecto

    def __str__(self) -> str:
        return self.title


