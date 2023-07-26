from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import UserModel
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views, login

from ProjectProtect.movie_auth.forms import RegisterForm


# Create your views here.


class RegisterView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    extra_context = {
        'form': form_class,
        'title': 'Register',
        'link_title': 'Login'
    }

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginView(auth_views.LoginView):
    template_name = 'app_auth/login.html'
    UserModel = get_user_model()
    login_url = 'app_auth/login.html'
    extra_context = {
        'title': 'login',
        'link_title': 'Register'
    }


class LogoutView(auth_views.LogoutView):
    template_name = 'app_auth/logout.html'


class EditProfileView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'app_auth/edit-profile.html'
    user = get_user_model()
    extra_context = {
        'user': user,
    }
