from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField()
    aqi = models.IntegerField()

class Log(models.Model):
    OPTIONS = (
        ('B', 'Breathe Deeper'),
        ('D', "Don't Inhale"),
        ('M', 'Mask Up')
    )
    date = models.DateField('Date')
    option = models.CharField(
        max_length=1,
        choices=OPTIONS,
        default=OPTIONS[0][0]
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_option_display()} on {self.date}"