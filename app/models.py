from django.db import models
import datetime

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255, default="Anonymous", null=True)
    created_date = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    modified_date = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    modified_date = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

class Quote(models.Model):
    author = models.ForeignKey(Author)
    comment = models.ForeignKey(Comment, null=True)
    quote = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    modified_date = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    def __unicode__(self):
        return ''.join(['\"', self.quote, '\"', ' -', self.author.name])

