import datetime

from django.db import models


class Positions(models.Model):
    Position = models.CharField(max_length=10)
    Type = models.CharField(max_length=3)
    Entry = models.FloatField()
    Exit = models.FloatField()
    PL = models.FloatField()
    EntryDateTime = models.DateTimeField()
    ExitDateTime = models.DateTimeField()
