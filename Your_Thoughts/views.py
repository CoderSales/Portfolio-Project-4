from django.shortcuts import render


# Create your views here.
def get_comment(user_request):
    return render(user_request, 'Your_Thoughts/comment-page.html')
