from django.db import models
from django.urls import reverse

# Create your models here.


class Wish(models.Model):
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('index')
