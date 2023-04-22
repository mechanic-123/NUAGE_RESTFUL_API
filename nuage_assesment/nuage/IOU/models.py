import jsonfield
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owes = jsonfield.JSONField()
    owedby = jsonfield.JSONField()
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
