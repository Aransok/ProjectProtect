import re

from django import forms
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic as views

from ProjectProtect.moviesite.forms import MovieModelForm, CommentForm
from ProjectProtect.moviesite.models import MovieModel, Comment


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
        'movies': movies
    }

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
