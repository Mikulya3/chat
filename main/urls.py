from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title = 'Messenger',
        default_version='1',
        description='online'    
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger/',schema_view.with_ui('swagger')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)