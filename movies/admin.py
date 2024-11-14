from django.contrib import admin
from .models import Movie, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'country', 'rating', 'category')
    search_fields = ('title', 'description', 'genre', 'director', 'actors')
    list_filter = ('category', 'year', 'rating')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user_name', 'rating', 'created_at')
    search_fields = ('user_name', 'comment', 'movie__title')
    list_filter = ('movie', 'rating')
