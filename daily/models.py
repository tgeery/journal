from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=200, default='title')
    date = models.DateTimeField('date published', default=0)
