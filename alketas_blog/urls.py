
from django.contrib import admin
from django.urls import path, include

from .views import index




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/', include('user_account.urls')),
    path('api/', include('user_profile.urls')),
    path('api/', include('blog.urls')),
] 