# Generated by Django 4.2 on 2024-11-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_remove_movie_dislikes_count_remove_movie_likes_count_and_more'),
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
        migrations.DeleteModel(
            name='MovieReaction',
        ),
    ]
