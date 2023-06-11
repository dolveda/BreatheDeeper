from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)

class City(models.Model):
    name = models.CharField()
    aqi = models.IntegerField()