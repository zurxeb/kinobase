from django.conf.urls.static import static
from django.urls import path
from moviebase import settings
from . import views
from .views import movie_detail, add_movie, kino, serial, anime, multfilm

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('film/<int:pk>/', movie_detail, name='movie_detail'),
    path('add_movie/', add_movie, name='add_movie'),
    path('kino/', kino, name='kino'),
    path('serial/', serial, name='serial'),
    path('anime/', anime, name='anime'),
    path('multfilm/', multfilm, name='multfilm'),
    path('about/', views.about, name='about'),
    path('movie/<int:movie_id>/like_dislike/', views.like_dislike_movie, name='like_dislike'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
