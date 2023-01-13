from django.db import models
from django.urls import reverse


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}'

    def get_absolute_url(self):
        return reverse('home')