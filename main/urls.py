from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib.auth.views import LoginView

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
    path('swagger/',schema_view.with_ui('swagger')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('chats/', include('mychatapp.urls')),
    path('account/', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

