from django.urls import path
from .views import LoginView, GetUsers, RegisterView, logoutView, GetAuth

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('get_users/', GetUsers.as_view(), name='get_users'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logoutView, name='logout'),
    path('get_auth/', GetAuth.as_view(), name='get_auth'),
]
