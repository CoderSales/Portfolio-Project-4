from django.test import TestCase
from .models import Post

# Create your tests here.


class TestViews(TestCase):

    def test_get_Post(self):
        user_response = self.client.get('/')
        self.assertEqual(user_response.status_code, 200)
        self.assertTemplateUsed(user_response, 'Your_Thoughts/comment-page.html')

    def test_get_add_Post_page(self):
        user_response = self.client.get('/add')
        self.assertEqual(user_response.status_code, 200)
        self.assertTemplateUsed(user_response, 'Your_Thoughts/add_post.html')

    def test_get_edit_Post_page(self):
        post = Post.objects.create(name='Test Post')
        user_response = self.client.get(f'/edit/{post.id}')
        self.assertEqual(user_response.status_code, 200)
        self.assertTemplateUsed(user_response, 'Your_Thoughts/edit_post.html')

    def test_can_add_Post(self):
        user_response = self.client.post('/add', {'name': 'Test Added Post'})
        self.assertRedirects(user_response, '/')

    def test_can_delete_Post(self):
        post = Post.objects.create(name='Test Post')
        user_response = self.client.get(f'/delete/{post.id}')
        self.assertRedirects(user_response, '/')
        existing_posts = Post.objects.filter(id=post.id)
        self.assertEqual(len(existing_posts), 0)
        
    def test_can_toggle_Post(self):
        post = Post.objects.create(name='Test Post', done=True)
        user_response = self.client.get(f'/toggle/{post.id}')
        self.assertRedirects(user_response, '/')
        updated_post = Post.objects.get(id=post.id)
        self.assertFalse(updated_post.done)
