"""
sets out the views for Django website user
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm
from django.views import generic, View
# from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

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
    """
    add toggle functionality from done to not
    """

    post = get_object_or_404(Post, id=post_id)
    post.done = not post.done
    post.save()
    return redirect('get_comment')


def delete_post(user_request, post_id):
    """
    add delete button for post
    """

    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('get_comment')
