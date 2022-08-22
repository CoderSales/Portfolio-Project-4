"""Profile_Project_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

https://stackoverflow.com/questions/11439447/django-import-views-from-separate-apps/45609168

"""
from django.contrib import admin
from django.urls import path, include
from Your_Thoughts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add', views.add_post, name='add'),
    path('edit/<post_id>', views.edit_post, name='edit'),
    path('toggle/<post_id>', views.toggle_post, name='toggle'),
    path('delete/<post_id>', views.delete_post, name='delete'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('Your_Thoughts.urls'), name='Your_Thoughts_urls'),
    path('accounts/', include('allauth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]
