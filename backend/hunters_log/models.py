from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=264)
    address = models.CharField(max_length=264)
    city = models.CharField(max_length=264)
    state = models.CharField(max_length=264)
    zip = models.CharField(max_length=10)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Game(models.Model):

    MAMMAL = 'mammal'
    BIRD = 'bird'
    FISH = 'fish'

    GAME_CHOICES = (
        (MAMMAL, 'Mammal'),
        (BIRD, 'Bird'),
        (FISH,'Fish'),
    )

    MALE = 'male'
    FEMALE = 'female'

    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    name = models.CharField(max_length=264)
    classification = models.CharField(max_length=264, choices=GAME_CHOICES)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    def __str__(self):
        return self.name

class Log(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.date
