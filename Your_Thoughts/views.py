from django.shortcuts import render, redirect
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


def add_post(user_request):
    if user_request.method == 'POST':
        name = user_request.POST.get('comment_name')
        done = 'done' in user_request.POST
        Post.objects.create(name=name, done=done)

        return redirect('get_comment')
    return render(user_request, 'Your_Thoughts/add_post.html')