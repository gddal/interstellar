from django.db import models
from datetime import datetime

class Orders(models.Model):
    total = models.FloatField()
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coordinatesX = models.FloatField(blank=False, default=0)
    coordinatesY = models.FloatField(blank=False, default=0)
    date_hour_product = models.DateTimeField(blank=False, default=None)
    constellations = models.BooleanField(default=True)
