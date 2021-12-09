import datetime

from django.db import models


class Position(models.Model):
    Option = models.CharField(max_length=10)
    Type = models.CharField(max_length=3)
    Entry = models.FloatField()
    Exit = models.FloatField(default=None, blank=True, null=True)
    PL = models.FloatField(default=None, blank=True, null=True)
    EntryDateTime = models.DateTimeField(default=None, blank=True, null=True)
    ExitDateTime = models.DateTimeField(default=None, blank=True, null=True)
