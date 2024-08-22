from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import Post
from .serializers import FeedSerializer, CreatePostSerializer, GetPostSerializer
from .utils import create_post

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView



class FeedView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = FeedSerializer


class CreatePostView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreatePostSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            author = request.user
            title = serializer.validated_data['title']
            body = serializer.validated_data['body']
            created_at = serializer.validated_data.get('created_at')

            try:
                post = create_post(
                    author=author,
                    title=title,
                    body=body,
                    created_at=created_at
                )
                return Response({'message': 'پست با موفقیت ساخته شد'}, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except PermissionError as e:
                return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetPosts(ListAPIView):
    serializer_class = GetPostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

