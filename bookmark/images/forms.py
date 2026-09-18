from urllib.parse import urlparse
import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png', 'webp', 'gif']

        # Parse the URL and look only at the path (ignores ?query and #fragment)
        path = urlparse(url).path
        if '.' not in path:
            raise forms.ValidationError('The given URL does not match valid image extensions.')

        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']

        # Same parsing trick here
        path = urlparse(image_url).path
        extension = path.rsplit('.', 1)[1].lower() if '.' in path else 'jpg'

        name = slugify(image.title)
        # extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        # Download image form the given URL
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        image.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image.save()
        return image
