from django.test import TestCase
from .models import Post


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        post = Post.objects.create(name='Test Post')
        self.assertFalse(post.done)

    def test_Post_string_method_returns_name(self):
        post = Post.objects.create(name='Test Post')
        self.assertEqual(str(post), 'Test Post')
