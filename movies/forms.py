from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title', 'description', 'year', 'country', 'genre', 'director',
            'actors', 'rating', 'duration', 'age_limit', 'category', 'poster', 'trailer_link'
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']

