from django.shortcuts import render
from .models import Post


# Create your views here.
def get_comment(user_request):
    print("hello")
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    # print(posts)
    return render(user_request, 'Your_Thoughts/comment-page.html', context)
