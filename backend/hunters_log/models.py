from django.db import models

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
    name = models.CharField(max_length=264)
    classification = models.CharField(max_length=264)
    sex = models.CharField(max_length=264)

    def __str__(self):
        return self.name

class Log(models.Model):
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    game = models.ForeignKey(Game)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.date
