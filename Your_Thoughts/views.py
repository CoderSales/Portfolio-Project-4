from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm, CommentForm


class PostList(generic.ListView):
    """
    Post List
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    Open Detail on Post
    """
    def get(self, request, slug, *args, **kwargs):
        "get"
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        "post"
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(View):
    "Post Like class"
    def post(self, request, slug, *args, **kwargs):
        "post"
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


#  moved up functions before classes for file (urls.py Your_Thoughts)


class PostEdit(View):
     def get(self, request, slug, *args, **kwargs):
        "get"
        post = get_object_or_404(Post, slug=slug)
        form = PostForm(instance=post)
        context = {
            'form': form
        }
        return render(request, 'Your_Thoughts/edit_post.html', context)




def get_comment(user_request):
    """
    sets out how to get comment passing in user_request
    """

    print("hello")
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
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


# def index2(View):
#     def get(self, request, slug, *args, **kwargs):
#         "get"
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.order_by('-created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": False,
#                 "liked": liked,
#                 "comment_form": CommentForm(),
#             },
#         )

#     def post(self, request, slug, *args, **kwargs):
#         "post"
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.order_by('created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True
#         else:
#             post.likes.add(request.user)