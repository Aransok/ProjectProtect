from django.template.defaulttags import comment
from django.urls import path

from ProjectProtect.moviesite import views
from ProjectProtect.moviesite.views import MovieList, MovieDetails, GenreMoviesView, add_comment, delete_comment

urlpatterns = [
    path('', MovieList.as_view(), name='home'),
    path('details/<int:pk>-<slug:slug>/', MovieDetails.as_view(), name='movie_details'),
    path('movies/genre/<str:genre>/', GenreMoviesView.as_view(), name='movies_by_genre'),
    path('movies/add/comment/<int:pk>-<slug:slug>/', add_comment, name= "comment"),
    path('movies/delete/comment/<int:pk>-<slug:slug>/', delete_comment, name= "delete_comment")
]