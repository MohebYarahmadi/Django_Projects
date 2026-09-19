from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings


class Profile(models.Model):
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    # Relations
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Profile of {self.user.username}'


class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    user_form = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rel_from_set')
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rel_to_set')


    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.user_form} follows {self.user_to}'




# Add the following field to User dynamically
user_model = get_user_model()
user_model.add_to_class(
    'following', models.ManyToManyField('self', through=Contact, symmetrical=False, related_name='followers')
)
