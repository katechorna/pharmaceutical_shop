from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import static

from django.conf import settings


urlpatterns = [
    path('', include('shop.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
