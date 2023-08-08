from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views, login

from ProjectProtect.movie_auth.forms import RegisterForm, UserProfileForm
from ProjectProtect.movie_auth.models import Profile


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


from django.shortcuts import render, redirect
from .forms import UserProfileForm


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('edit-profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'app_auth/edit-profile.html', {'form': form})
