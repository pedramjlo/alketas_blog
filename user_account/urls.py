from django.urls import path
from .views import LoginView, GetUsers, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('get_users/', GetUsers.as_view(), name='get_users'),
    path('register/', RegisterView.as_view(), name='register'),
]
