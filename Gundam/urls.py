from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grade/', include('grade.urls')),
    path('universe/', include('universe.urls')),
    path('series/', include('series.urls')),
    path('pilot/', include('pilot.urls')),
    path('gundam_data/', include('gundam_data.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
