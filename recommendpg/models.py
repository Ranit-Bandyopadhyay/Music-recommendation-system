from django.db import models
import songs as s
# Create your models here.
class Tracks(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    art = models.CharField(max_length=500)
    artist = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

