from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models


class ItemBase(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relations
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_related')


    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_created')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # Relations
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')


class Content(models.Model):
    object_id = models.PositiveIntegerField()

    # Relations
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in':('text', 'video', 'image', 'file')
        }
    )

    # Generic Relations
    item = GenericForeignKey('content_type', 'object_id')
