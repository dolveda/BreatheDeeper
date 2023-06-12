from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField()
    coordinates = models.CharField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'pk': self.id})
    
class Profile(models.Model):
    name = models.CharField(max_length=50)
    cities = models.ManyToManyField(City)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'profile_id': self.id})


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

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_option_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']