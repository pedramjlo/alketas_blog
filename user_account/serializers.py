from rest_framework import serializers
from .models import CustomUser


from rest_framework import serializers
from django.contrib.auth import authenticate, login
from .models import CustomUser



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("این کاربر وجود ندارد یا غیرفعال است")
        else:
            raise serializers.ValidationError("فیلدهای نام کاربری و گذرواژه نباید خالی باشند")

        data["user"] = user
        return data





class GetUserSerializer(serializers.ModelSerializer):
    user_role = serializers.CharField(source='profile.role', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'user_role',)





class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')




class GetAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username')