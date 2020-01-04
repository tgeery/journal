from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=200, default='title')
    date = models.DateTimeField('date published', default=0)
    header1 = models.CharField(max_length=200, default='')
    context1 = models.CharField(max_length=200, default='', null=True, blank=True)
    header2 = models.CharField(max_length=200, default='', null=True, blank=True)
    context2 = models.CharField(max_length=200, default='', null=True, blank=True)
    header3 = models.CharField(max_length=200, default='', null=True, blank=True)
    context3 = models.CharField(max_length=200, default='', null=True, blank=True)
