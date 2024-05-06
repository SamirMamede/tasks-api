from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.getUsers, name='get_all_users'),
    path('registration/', views.registerUser, name='register_new_user'),
]