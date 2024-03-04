from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializers
from .models import Movie
# Create your views here.

class MovieListViewClass(generics.ListAPIView) :
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

class MovieFilterByCategoryClass(generics.ListAPIView) :
    serializer_class = MovieSerializers

    def get_queryset(self):
        category = self.kwargs.get('categories')
        queryset = Movie.objects.filter(category__iexact=category)
        return queryset
