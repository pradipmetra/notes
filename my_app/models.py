from django.db import models

class member(models.Model):
    Name = models.CharField(max_length=15)
    Email = models.CharField(max_length=25)
    Password = models.CharField(max_length=6)