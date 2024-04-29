from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="InovaTask API Documentation",
        default_version='v1',
        description="API Documentation",
        contact=openapi.Contact(email="https://wa.me/5592992422202?text=Hello+World%21+"),
    ),
    public=True,
)

urlpatterns = [
    path('', include('api.urls')),
    path('registration', include('registration.urls')),
    path('auth/api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
