
from django.contrib import admin
from django.urls import path, include






urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_account.urls')),
    path('api/', include('user_profile.urls')),
    path('api/', include('blog.urls')),
] 