from django.urls import path
from .views import FeedView, CreatePostView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('create_post/', CreatePostView.as_view(), name='create_view'),
]
