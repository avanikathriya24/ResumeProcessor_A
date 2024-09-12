from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, extract_resume

urlpatterns = [
    path('', home, name='home'),
    path('api/extract_resume/', extract_resume, name='extract_resume'),
]

# Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
