from django.urls import path
from .views import SelectAvatar, GetProfiles

urlpatterns = [
    path('select-avatar/', SelectAvatar.as_view(), name='select-avatar'),
    path('get-profiles/', GetProfiles.as_view(), name='get-profiles'),
    
]
