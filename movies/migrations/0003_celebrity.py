# Generated by Django 4.2 on 2024-10-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='celebrities/')),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]