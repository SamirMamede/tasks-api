from django.urls import path, include
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
    path('auth/', include('authentication.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
