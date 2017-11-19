from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.conf import settings
from like.models import LikeDislike

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    categories = models.ManyToManyField(Category, related_name="blogs")

    def __str__(self):
        return '{0} (created at: {1})'.format(self.name, self.created_at)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey(Blog, related_name='posts')
    likes = GenericRelation(LikeDislike)

    def __str__(self):
        return '{0} (created at: {1})'.format(self.name, self.created_at)