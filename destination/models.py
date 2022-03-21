from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

TEXT_MAX_LENGTH = 300
NAME_MAX_LENGTH = 100

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    about = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True)

    def __str__(self):
        return self.user.username


class Destination(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True)
    image = models.ImageField(upload_to='destination_images', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Destination, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Destinations'

    def __str__(self):
        return self.name
    