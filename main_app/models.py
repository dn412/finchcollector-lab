from django.db import models
# need the reverse method from django urls for redirects
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.IntegerField()

    def __str__(self):
        return self.name
    # this is used for redirects from class based views
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})