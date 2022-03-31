from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings

TEXT_MAX_LENGTH = 300
NAME_MAX_LENGTH = 100

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    about = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True)

    def __str__(self):
        return self.user.username

DESTINATION_TYPES = [('H', 'History'), ('S', 'Sport'), ('R', 'Relax'), ('O', 'Other')]

class Destination(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True)
    image = models.ImageField(upload_to='destination_images', blank=True)
    destination_type = models.CharField(max_length=1, choices=DESTINATION_TYPES, default='O')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Destination, self).save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def total_rating(self):
        comments = Comment.objects.filter(destination=self)
        rating_total = 0
        if comments.count() == 0:
            return 0
        else:
            for rating in comments:
                rating_total += rating.rate
            return round(rating_total/comments.count(), 2)

    class Meta:
        verbose_name_plural = 'Destinations'

    def __str__(self):
        return self.slug
    
Rate_Choices = [(1, '1 - Not good'), (2, '2 - Average'), (3, '3 - Good'), (4, '4 - Very good'), (5, '5 - Excellent')]
class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(choices=Rate_Choices, blank=True, null=True)
        
    def __str__(self):
        return '%s - %s' % (self.user.username, self.destination.name)
 