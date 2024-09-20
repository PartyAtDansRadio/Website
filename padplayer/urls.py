from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.views import PlayerView

urlpatterns = [
    path('', PlayerView.as_view(), name='player'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)