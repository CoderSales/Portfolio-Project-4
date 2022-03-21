from django.test import TestCase
from .models import Post


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        post = Post.objects.create(name='Test Post')
        self.assertFalse(post.done)