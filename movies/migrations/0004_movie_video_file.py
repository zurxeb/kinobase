# Generated by Django 4.2 on 2024-10-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_celebrity'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='movies/'),
        ),
    ]
