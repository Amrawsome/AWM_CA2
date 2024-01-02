from django.db import models

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.name

