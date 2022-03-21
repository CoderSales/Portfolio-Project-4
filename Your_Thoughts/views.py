from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm



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
        form = PostForm(user_request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_comment')
    form = PostForm()
    context = {
        'form': form
    }
    return render(user_request, 'Your_Thoughts/add_post.html', context)