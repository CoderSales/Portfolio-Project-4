from . import views

from django.contrib import admin
from django.urls import path, include
# from Your_Thoughts import views

urlpatterns = [

    # path('', views.get_comment, name='get_comment'),

    # path('add', views.add_post, name='add'),
    # path('edit/<post_id>', views.edit_post, name='edit'),
    # path('toggle/<post_id>', views.toggle_post, name='toggle'),
    # path('delete/<post_id>', views.delete_post, name='delete'),
    # path('summernote/', include('django_summernote.urls')),
    # path('', include('Your_Thoughts.urls'), name='Your_Thoughts_urls'),
    # path('accounts/', include('allauth.urls')),
]

urlpatterns = [
    # cannot seemingly have two roots, so line not working but page loads
    # path('', include('Your_Thoughts.urls'), name='Your_Thoughts_urls'),

    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('', views.get_comment, name='get_comment'),
    path('add', views.add_post, name='add'),

    path('edit/<post_id>', views.edit_post, name='edit'),
    path('toggle/<post_id>', views.toggle_post, name='toggle'),
    path('delete/<post_id>', views.delete_post, name='delete'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    # path('admin/', admin.site.urls),
    # path('add', views.add_post, name='add'),
]
