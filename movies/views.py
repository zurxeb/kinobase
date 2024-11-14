from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, Celebrity
from .forms import MovieForm, ReviewForm

# Create your views here.
from django.shortcuts import render
from .models import Movie


# views.py
from django.shortcuts import get_object_or_404, redirect

def like_dislike_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'like':
            movie.likes_count += 1
        elif action == 'dislike':
            movie.dislikes_count += 1
        movie.save()
    return redirect('movies:movie_detail', pk=movie.pk)
def home(request):

    celebrities = Celebrity.objects.all()
    latest_movies = Movie.objects.order_by('-id')[:5]
    star_range = range(1, 6)
    movies = Movie.objects.all()
    search = request.GET.get('q')
    if search:
        movies = Movie.objects.filter(title__icontains=search)
    else:
        movies = Movie.objects.all()


    categories = ['anime', 'kino', 'serial', 'multfilm']
    categorized_movies = {category: movies.filter(category=category) for category in categories}

        # Har bir kategoriya uchun 3 tadan guruhlash
    for category, movie_list in categorized_movies.items():
        categorized_movies[category] = [movie_list[i:i + 3] for i in range(0, len(movie_list), 3)]

    context = {
            'celebrities': celebrities,
            'latest_movies': latest_movies,
            'categorized_movies': categorized_movies,
            'star_range': star_range,
            'movies': movies,
    }



    return render(request, 'home.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('movies:movie_detail', pk=movie.pk)
    else:
        review_form = ReviewForm()

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'review_form': review_form,
    })
def add_movie(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = MovieForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('movies:home')
        else:
            form = MovieForm()
        return render(request, 'add-movie.html', {'form': form})
    else:
        return redirect('movies:home')



def kino(request):
    movies = Movie.objects.filter(category='kino')
    return render(request, 'kino.html', {'movies': movies})

def serial(request):
    movies = Movie.objects.filter(category='serial')
    return render(request, 'serial.html', {'movies': movies})

def anime(request):
    movies = Movie.objects.filter(category='anime')
    return render(request, 'anime.html', {'movies': movies})

def multfilm(request):
    movies = Movie.objects.filter(category='multfilm')
    return render(request, 'multfilm.html', {'movies': movies})

def about(request):
    return render(request,'about.html')