"""
import models
"""
import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # LMS Django Blog 006b: Building The Models


STATUS = ((0, "Draft"), (1, "Published"))  # LMS Django Blog 006b: Building The Models


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # new_field = models.CharField(max_length=140, default='SOME STRING', blank=True)
    # slug = models.SlugField(max_length=200, unique=True, default='SOME STRING', blank=True)
    # slug = models.SlugField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default='string')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(default='text')
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #, default='author'
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_likes', blank=True)
    
    name = models.CharField(max_length=50, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        ordering = ["-created_on"]

    # Note:
    # in
    # PROBLEMS in Console View
    # __str__ does not return str
    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
