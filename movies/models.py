from django.db import models

from users.models import CustomUser


class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('kino', 'Kino'),
        ('anime', 'Anime'),
        ('serial', 'Serial'),
        ('multfilm', 'Multfilm'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=300)
    rating = models.FloatField()
    duration = models.CharField(max_length=20)
    age_limit = models.CharField(max_length=10)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    poster = models.ImageField(upload_to='posters/')
    trailer_link = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='movies/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title


class LikeDislike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=[('like', 'Like'), ('dislike', 'Dislike')])

    class Meta:
        unique_together = ('user', 'movie')  # Ensures a user can only like/dislike a movie once

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user_name} for {self.movie.title}'
from django.db import models

class Celebrity(models.Model):
    name = models.CharField(max_length=100)  # Mashhur shaxsning ismi
    image = models.ImageField(upload_to='celebrities/')  # Rasmni saqlash joyi
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)  # Reyting, masalan 4.5
    bio = models.TextField(blank=True)  # Biografiya (ixtiyoriy)

    def __str__(self):
        return self.name
