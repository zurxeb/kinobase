# Generated by Django 4.2 on 2024-11-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='dislikes_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
