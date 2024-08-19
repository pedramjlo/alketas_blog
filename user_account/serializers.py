from rest_framework import serializers
from .models import CustomUser


from rest_framework import serializers
from django.contrib.auth import authenticate
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
                raise serializers.ValidationError("Invalid login credentials.")
        else:
            raise serializers.ValidationError("Must include both username and password.")

        data["user"] = user
        return data




class GetUsers(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')