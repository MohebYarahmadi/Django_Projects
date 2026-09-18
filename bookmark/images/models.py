from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Image(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    # The owner of the uploaded image
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images_created')
    # Who likes it
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='images_liked')

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']

    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*arg, **kwargs)

    def get_absolute_url(self):
        return reverse('image:detail', args=[self.id, seld.slug])

    def __str__(self):
        return self.title
