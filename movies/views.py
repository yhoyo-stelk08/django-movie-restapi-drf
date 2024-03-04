from django.shortcuts import render
from drf.models import Movie
# Create your views here.

def list_movie(request) :
    movies = Movie.objects.all()
    ctx = {
        'title' : 'List of Movies',
        'movies' : movies,
    }
    return render(request,'movies/index.html',ctx)