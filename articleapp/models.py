from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime


class Article(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    headline=models.CharField(max_length=100)
    content=models.TextField()
    pub_date=models.DateField()
    article_created=models.DateTimeField(auto_now_add=True)
    modified_on=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('article-list')
