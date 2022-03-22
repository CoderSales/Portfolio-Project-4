"""
import models
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # LMS Django Blog 006b: Building The Models


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))  # LMS Django Blog 006b: Building The Models



class Post(models.Model):
    # https://stackoverflow.com/questions/7877522/how-do-i-disable-missing-docstring-warnings-at-a-file-level-in-pylint
    """
    allows creation of a post with name comment text and Completed fields
    """
    # LMS Django Blog 006b: Building The Models:
    title = models.CharField(max_length=200, unique=True)
    slug = models.Slugfield(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    # above, "on_delete=CASCADE" in Foreign Key
    # means that if the one record in the 
    # one-to-many relationship 
    # is deleted, then the 
    # related records will be deleted too.
    # So deleting a user will also 
    # delete their blog posts.
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    # https://tutorial-extensions.djangogirls.org/en/homework_create_more_models
    comment = models.TextField(null=False, blank=False)
    # created_date = models.DateTimeField(default=timezone.now)
    # LMS
    done = models.BooleanField(null=False, blank=False, default=False)

    # Note:
    # in
    # PROBLEMS in Console View
    # __str__ does not return str
    def __str__(self):
        return self.name
