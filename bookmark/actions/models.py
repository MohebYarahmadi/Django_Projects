from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.db import models


class Action(models.Model):
    verb = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actions')

    # Generic Relation
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE, related_name='target_obj')
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['target_ct', 'target_id']),
        ]
        ordering = ['-created_at']
