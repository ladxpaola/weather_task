from django.db import models

class WeatherResponse(models.Model):
    doy = models.IntegerField()
    events = models.JSONField()