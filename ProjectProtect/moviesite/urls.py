from django.urls import path

from ProjectProtect.moviesite import views
from ProjectProtect.moviesite.views import MovieList, MovieDetails, GenreMoviesView, add_comment, delete_comment, \
    MovieEdit

urlpatterns = [
    path('', MovieList.as_view(), name='home'),
    path('details/<int:pk>-<slug:slug>/', MovieDetails.as_view(), name='movie_details'),
    path('movies/genre/<str:genre>/', GenreMoviesView.as_view(), name='movies_by_genre'),
    path('movies/add/comment/<int:pk>-<slug:slug>/', add_comment, name= "comment"),
    path('movies/delete/comment/<int:pk>-<slug:slug>/', delete_comment, name= "delete_comment"),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('edit/<int:pk>-<slug:slug>/', MovieEdit.as_view(), name='movie_edit'),
    path('movie/<int:pk>/<slug:slug>/delete/', views.delete_movie, name='delete_movie'),
    path('add_to_watchlist/<int:pk>-<slug:slug>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<int:pk>-<slug:slug>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('like_movie/<int:pk>-<slug:slug>/', views.like_movie, name='like_movie'),
    path('user-movies/', views.user_profile, name='user_movies'),
]
