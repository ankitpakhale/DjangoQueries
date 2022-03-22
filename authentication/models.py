from django.db import models

# Create your models here.

class userDetails(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField(default='')
    address = models.CharField(max_length=300, default='')
    password = models.CharField(default='', max_length=15)
    def __str__(self):
        return self.name