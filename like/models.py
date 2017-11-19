from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
# Create your models here.


class LikeDislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="likes")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return 'by {0} #id{1}'.format(self.user, self.id)
