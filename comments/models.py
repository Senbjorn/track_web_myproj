from django.db import models
from django.conf import settings
from blog.models import Post
# Create your models here.


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(default='')
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')

    def __str__(self):
        return 'comment #id{0} created at {1} by {2}'.format(self.id, self.created_at, self.author)