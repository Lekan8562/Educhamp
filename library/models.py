from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class 
class Book(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    isbn = models.IntegerField(max_length=13)
    authors = models.ManyToManyField(User,related_name='author_books')
    location = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        ordering = 'published'
    def __str__(self):
        return self.name    