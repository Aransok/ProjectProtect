from django.urls import path

from ProjectProtect.movie_auth.views import RegisterView, LoginView, LogoutView, EditProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile'),
]