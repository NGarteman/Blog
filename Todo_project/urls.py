from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tasks_app.urls')),
    path('category/', include('Categories_app.urls')),
    path('account/', include('accounts_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
