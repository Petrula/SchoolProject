from django.db import models

class People(models.Model):
    name = models.CharField(max_length=16)
    phone = models.CharField(max_length=20)
    sport_section = models.CharField(max_length=20, null=True)

