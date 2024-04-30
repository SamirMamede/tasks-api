from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registerUser, name='register_new_user'),
]