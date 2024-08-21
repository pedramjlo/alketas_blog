
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^.*$', IndexView.as_view(), name='index'),
    path('api/', include('user_account.urls')),
    path('api/', include('user_profile.urls')),
    path('api/', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
