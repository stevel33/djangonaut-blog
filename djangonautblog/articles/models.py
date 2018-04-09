# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # built in function that defines how an Article will look
    # when making database query
    # self is the instance of the Article
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
