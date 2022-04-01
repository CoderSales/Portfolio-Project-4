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
from home.views import index as index1
from Your_Thoughts.views import index as index2
# from Profile_Project_4.templates import index as indexProj
from django.conf import settings
from django.conf.urls.static import static
# from . import views
# import home
# import home
# from home import products as products1


urlpatterns = [
    # #1 path('admin/', home.admin.site.urls),
    path('admin/', admin.site.urls),
    # path('add', views.add_post, name='add'),
    # path('edit/<post_id>', views.edit_post, name='edit'),
    # path('toggle/<post_id>', views.toggle_post, name='toggle'),
    # path('delete/<post_id>', views.delete_post, name='delete'),
    # # path('summernote/', include('django_summernote.urls')),
    # # path('', include('Your_Thoughts.urls'), name='Your_Thoughts_urls'),
    # path('accounts/', include('allauth.urls')),
    # #2 path('accounts/', home.include('allauth.urls')),

    # # path('althome2', views.index, name='home'),
    # # path('', views.index, name='Your_Thoughts'), # duplicated from above
    # #3 path('', home.views.index, name='home.urls'),
    # path('', index1, name='home.urls'),
    path('', index2, name='Your_Thoughts.urls'),
    # path('', views.index, name='Your_Thoughts.urls'),


    # path('', views.get_comment, name='get_comment'),
    # path('option2', indexProj.get_comment, name='get_comment'),

    # path('products/', include('products.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
