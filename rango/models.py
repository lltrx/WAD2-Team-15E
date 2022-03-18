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
    
    '''
class Place(models.Model):
    # Change this one to places
    category = models.ForeignKey(Destination, on_delete=models.CASCADE)
    title = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.URLField()


    def __str__(self):
        return self.title


class Category(models.Model):
    # Need to be change for helpful categories for our Project
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    # Change this one to places
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # Keep this and add more to it
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
'''