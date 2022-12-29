from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.name

