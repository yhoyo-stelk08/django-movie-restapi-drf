from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('list/',views.list_movie,name='movie-list'),
]
