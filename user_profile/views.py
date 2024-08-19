from django.shortcuts import render

from .models import Avatar, Profile
from .serializers import AvatarChoiceSerializer, GetProfileSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import UpdateAPIView, ListAPIView




class SelectAvatar(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Avatar.objects.all()
    serializer_class = AvatarChoiceSerializer


    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            if not user is None:
                user.avatar = serializer.validated_data['image']
                user.save()
                return Response({'message': 'Profile avatar changed successfully'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'user not found!'}, status=status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class GetProfiles(ListAPIView):
    serializer_class = GetProfileSerializer
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()