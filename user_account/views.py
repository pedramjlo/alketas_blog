from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout

from .models import CustomUser
from .serializers import LoginSerializer, GetUserSerializer, RegisterSerializer


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated




@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if not user is None:
                login(request, user)
                return Response({'message': 'ورود موفقیت آمیز'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'مشخصات به اشتباه وارد شده'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




"""
Getting a list of all CustomUser model objects (user accounts)

"""


class GetUsers(ListAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = GetUserSerializer




    



class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            first_name = serializer.validated_data['username']
            last_name = serializer.validated_data['username']
            email = serializer.validated_data['username']
            password = serializer.validated_data['username']

            try:
                user = CustomUser.objects.create_user(
                    username=username, 
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )

                user.set_password = password
                user.save()

                if user:
                    login(request, user)
                    return Response({'message': 'حساب شما ساخته شد. در حال ورود...'}, status=status.HTTP_201_CREATED)
                else:
                    return ({'message': 'خظایی رخ داده است'})
                
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



"""

a separate view for logout 

"""
            

def logoutView(request):
    logout(request)
    return redirect('login')
     #return JsonResponse({'message': 'با موفقیت از حسابتان خارج شدید'})


"""

 GetAuth() check whether the user is authenticated or not

"""

class GetAuth(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return Response({"message": "You are currently logged in."}, status=status.HTTP_202_ACCEPTED)
        return Response({'message': 'You are not logged in!'}, status=status.HTTP_401_UNAUTHORIZED)