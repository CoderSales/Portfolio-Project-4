"""
forms
"""
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    "Post Form"
    class Meta:
        "Meta"
        model = Post
        fields = ['title', 'content', 'featured_image']


class CommentForm(forms.ModelForm):
    "Comment Form class"
    class Meta:
        "Meta class for Comment Form"
        model = Comment
        fields = ('body',)
