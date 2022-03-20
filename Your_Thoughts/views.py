from django.shortcuts import render, HttpResponse

# Create your views here.
def Hello_World(user_request):
    return HttpResponse("Hello")