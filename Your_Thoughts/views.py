from django.shortcuts import render, HttpResponse

# Create your views here.
def hello_world(user_request):
    return HttpResponse("Hello")