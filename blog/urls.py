from django.urls import path
from .views import FeedView, CreatePostView, GetPosts, PostView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('create_post/', CreatePostView.as_view(), name='create_view'),
    path('get_posts', GetPosts.as_view(), name='get_posts'),
    path('post_page', PostView.as_view(), name='post_page'),
]
