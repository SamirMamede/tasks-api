from django.contrib import admin
from django.urls import path, include
from .views import UserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path("registration/", UserCreate.as_view()),
    path('api-auth/', include("rest_framework.urls")),
]