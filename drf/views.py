from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializers
from .models import Movie
# Create your views here.

class MovieListViewClass(generics.ListAPIView) :
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers