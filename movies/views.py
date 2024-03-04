from django.shortcuts import render
from drf.models import Movie
from django.core.paginator import Paginator
# Create your views here.

def list_movie(request) :
    movies = Movie.objects.all().order_by('id')
    
    paginator = Paginator(movies,1) # get movie 1 movie per page
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    ctx = {
        'title' : 'List of Movies',
        'movies' : movies,
    }
    return render(request,'movies/index.html',ctx)