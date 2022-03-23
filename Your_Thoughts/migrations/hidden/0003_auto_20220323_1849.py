# Generated by Django 3.2 on 2022-03-23 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Your_Thoughts', '0002_auto_20220323_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='new_field',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='SOME STRING', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='string', on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
