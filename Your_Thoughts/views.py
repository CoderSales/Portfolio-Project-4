"""
sets out the views for Django website user
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


# Create your views here.
def get_comment(user_request):
    """
    sets out how to get comment passing in user_request
    """

    print("hello")
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    # print(posts)
    return render(user_request, 'Your_Thoughts/comment-page.html', context)


def add_post(user_request):
    """
    sets out how to add a post
    """

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


def edit_post(user_request, post_id):
    """
    sets out how the user can edit a post
    """

    post = get_object_or_404(Post, id=post_id)
    if user_request.method == 'POST':
        form = PostForm(user_request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('get_comment')
    form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(user_request, 'Your_Thoughts/edit_post.html', context)


def toggle_post(user_request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.done = not post.done
    post.save()
    return redirect('get_comment')


def delete_post(user_request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('get_comment')
