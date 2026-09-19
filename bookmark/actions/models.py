from django.conf import settings

from django.db import models


class Action(models.Model):
    verb = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actions')

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']
