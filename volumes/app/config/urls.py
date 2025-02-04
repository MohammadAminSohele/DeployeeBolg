from django.contrib import admin
from django.urls import path,include

from .import settings

from django.conf.urls.static import static

urlpatterns = [
    path('',include('Articles.urls')),
    path('',include('account.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)