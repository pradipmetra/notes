from django.db import models

class member(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=6)

class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    message = models.CharField(max_length=150)