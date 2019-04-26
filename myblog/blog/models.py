from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Article(models.Model):
    url =models.CharField(max_length=200,default='Title')
    content=models.TextField(null=True)
