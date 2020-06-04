from django.db import models

# Create your models here.
class Reference(models.Model):
    title = models.CharField(max_length=200, default='title')
    date = models.DateTimeField('date published', default=0)
