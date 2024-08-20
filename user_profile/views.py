from django.shortcuts import render

from .models import Avatar, Profile
from .serializers import AvatarChoiceSerializer, GetProfileSerializer
from .utils import check_image

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView




class SelectAvatar(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, *args, **kwargs):
        image = request.data.get('image')
        try:
            user = check_image(image, request)
            return Response({'message': 'آواتار با موفقیت انتخاب شدس'}, status=status.HTTP_200_OK)
        
        except ValueError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class GetProfiles(ListAPIView):
    serializer_class = GetProfileSerializer
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()