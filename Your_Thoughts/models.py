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
    
    # Error in terminal: 
    """You are trying to add a non-nullable field 'author' to post without a default; we can't do that (the database needs something to populate existing rows)."""
    # Solution Reference for subsequent code block
    # https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a
    # You need to provide a default value:
    # new_field = models.CharField(max_length=140, default='SOME STRING')



    
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    # remove , default=1 from end of above line
    # # above, "on_delete=CASCADE" in Foreign Key
    # # means that if the one record in the 
    # # one-to-many relationship 
    # # is deleted, then the 
    # # related records will be deleted too.
    # # So deleting a user will also 
    # # delete their blog posts.
    # updated_on = models.DateTimeField(auto_now=True)
    # # content = models.TextField(default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)

    # added directly from:
    # https://github.com/Code-Institute-Solutions/Django3blog/blob/master/04_building_the_models/blog/models.py
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # end of added directly from
    # https://github.com/Code-Institute-Solutions/Django3blog/blob/master/04_building_the_models/blog/models.py

    created_on = models.DateTimeField(auto_now_add=True) #, default='author'
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_likes', blank=True)
    
    # remove old fields from Hello Django tutorial:
    name = models.CharField(max_length=50, null=False, blank=False)
    # https://tutorial-extensions.djangogirls.org/en/homework_create_more_models
    # comment = models.TextField(null=False, blank=False)
    # created_date = models.DateTimeField(default=timezone.now)
    # LMS
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
