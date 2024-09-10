from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from .views import dashboard, landingPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name="dashboard"),
    path('landing_page/', landingPage, name="landing_page"),
    path('', landingPage, name="landing_page"),
    path('hq/', include('hq.urls')),
    path('managers/', include('managers.urls')),
    path('consumer/', include("consumers.urls")),
    path('authenticate/', include("user_auth.urls")),
    path('category/', include("category.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)