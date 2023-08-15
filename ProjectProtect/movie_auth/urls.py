from django.urls import path

from ProjectProtect.movie_auth import views
from ProjectProtect.movie_auth.views import RegisterView, LoginView, LogoutView, edit_profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('manage_uploaders/', views.manage_uploaders, name='manage_uploaders'),
    path('toggle_uploader_status/<int:user_id>/', views.toggle_uploader_status, name='toggle_uploader_status'),

]
