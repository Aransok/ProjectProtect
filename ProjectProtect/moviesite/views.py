import re

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views, View
from django.views.generic import UpdateView

from ProjectProtect.moviesite.forms import MovieModelForm, CommentForm
from ProjectProtect.moviesite.models import MovieModel, Comment, UserWatchlist, MovieLikes, MovieDisLikes


# Create your views here.


class MovieList(views.CreateView):
    login_url = 'auth_app/login.html'
    model = MovieModel
    template_name = 'homepage.html'
    success_url = 'homepage'
    extra_context = {
        'movies': MovieModel.objects.all(),

    }

    def get(self, request, *args, **kwargs):
        movies = MovieModel.objects.all()
        paginator = Paginator(movies, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'homepage.html', {'form': MovieModelForm, 'page_obj': page_obj})


class MovieDetails(views.View):
    template_name = 'movie_details.html'
    model = MovieModel
    movies = MovieModel.objects.all()
    form_class = Comment


    extra_context = {
        'movies': movies,
    }

    def get(self, request, pk, slug):
        movie = self.get_object()
        movie_likes = MovieLikes.objects.filter(movie=movie, liked=True).count()


        context = {
            'movie': movie,
            'youtube_video_id': self.get_youtube_video_id(movie.trailer),
            'comments': Comment.objects.all(),
            'movies': self.movies,
            'movie_likes': movie_likes,

        }
        return render(request,self.template_name , context=context)
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        pk = self.kwargs.get('pk')
        return get_object_or_404(MovieModel, pk=pk, slug=slug)

    def get(self, request, pk, slug):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        movie = get_object_or_404(MovieModel, pk=pk, slug=slug)
        context = {
            'movie': movie,
            'youtube_video_id': self.get_youtube_video_id(movie.trailer),
            'comments': Comment.objects.all(),
            'movies': MovieModel.objects.all
        }
        return render(request, self.template_name, context=context)

    def get_youtube_video_id(self, url):
        video_id = None

        patterns = [
            r'^https?:\/\/(?:www\.)?youtube\.com\/watch\?.*v=([^\s&]+)',
            r'^https?:\/\/(?:www\.)?youtu\.be\/([^\s&]+)',
            r'^https?:\/\/(?:www\.)?youtube\.com\/embed\/([^\s&]+)'
        ]
        for pattern in patterns:
            match = re.match(pattern, url)
            if match:
                video_id = match.group(1)
                break
        return video_id


class GenreMoviesView(views.View):
    template_name = 'movies_by_genre.html'
    paginate_by = 20

    def get(self, request, genre):
        movies = MovieModel.objects.filter(genre=genre)
        paginator = Paginator(movies, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {'page_obj': page_obj, 'genre': genre})


def add_comment(request, pk, slug):
    movie = get_object_or_404(MovieModel, pk=pk, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('movie_details', pk=pk, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'movie_details.html', {'form': form, 'movie': movie})


def delete_comment(request, pk, slug):
    movie = get_object_or_404(MovieModel, pk=pk, slug=slug)
    comment_id = request.POST.get('comment_id')

    try:
        comment = Comment.objects.get(pk=comment_id, user=request.user)
        comment.delete()
    except Comment.DoesNotExist:
        pass

    return redirect('movie_details', pk=pk, slug=slug)


def add_movie(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('home')
    else:
        form = MovieModelForm()
    return render(request, 'add_movie.html', {'form': form})


class MovieEdit(UserPassesTestMixin, UpdateView):
    model = MovieModel
    form_class = MovieModelForm
    template_name = 'edit-movie.html'

    def get_success_url(self):
        return reverse_lazy('movie_details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def test_func(self):
        user = self.request.user
        return user.is_superuser or (user.is_authenticated and user.userprofile.is_uploader)


def delete_movie(request, pk, slug):
    movie = get_object_or_404(MovieModel, pk=pk, slug=slug)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')
    return render(request, 'delete_movie.html', {'movie': movie})



def add_to_watchlist(request, pk, slug):
    movie = MovieModel.objects.get(pk=pk, slug=slug)
    UserWatchlist.objects.get_or_create(user=request.user, movie=movie)
    return redirect('movie_details', pk=pk, slug=slug)



def like_movie(request, pk, slug):
    movie = MovieModel.objects.get(pk=pk, slug=slug)
    like, created = MovieLikes.objects.get_or_create(user=request.user, movie=movie)
    if not like.liked:
        like.liked = True
        like.save()
    return redirect('movie_details', pk=pk, slug=slug)

@login_required
def user_profile(request):
    user = request.user
    watchlist = UserWatchlist.objects.filter(user=user)
    liked_movies = MovieLikes.objects.filter(user=user, liked=True)
    context = {
        'watchlist': watchlist,
        'liked_movies': liked_movies
    }
    return render(request,'user_movies.html', context=context)


def remove_from_watchlist(request, pk, slug):
    movie = MovieModel.objects.get(pk=pk, slug=slug)
    UserWatchlist.objects.filter(user=request.user, movie=movie).delete()
    return redirect('movie_details', pk=pk, slug=slug)

