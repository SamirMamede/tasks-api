from django.urls import path
from .views import UserCreate

urlpatterns = [
    path("registration/", UserCreate.as_view()),
]