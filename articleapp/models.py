from django.db import models
from django.urls import reverse
import datetime


class Article(models.Model):
    headline=models.CharField(max_length=100)
    content=models.TextField()
    pub_date=models.DateField()
    article_created=models.DateTimeField(auto_now_add=True)
    modified_on=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('article-list')
