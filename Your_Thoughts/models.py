"""
import models
"""
from django.db import models


# Create your models here.


class Post(models.Model):
    # https://stackoverflow.com/questions/7877522/how-do-i-disable-missing-docstring-warnings-at-a-file-level-in-pylint
    """
    allows creation of a post with name comment text and Completed fields
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    # https://tutorial-extensions.djangogirls.org/en/homework_create_more_models
    author = models.ForeignKey(null=False, blank=False)
    # created_date = models.DateTimeField(default=timezone.now)
    # LMS
    date = models.BooleanField(null=False, blank=False, default=False)

    # Note:
    # in
    # PROBLEMS in Console View
    # __str__ does not return str
    def __str__(self):
        return self.name
