from django.urls import path
from  . import views

app_name = 'drf'

urlpatterns = [
    path('movies/',views.MovieListViewClass.as_view(),name='movies'),
    path('movies/<str:categories>',views.MovieFilterByCategoryClass.as_view(),name='movie_by_category'),
]
