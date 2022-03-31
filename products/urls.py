# from django.contrib import admin
from django.urls import path
# from home import views
from . import views

urlpatterns = [
    path('', views.all_products, name='products')
]
