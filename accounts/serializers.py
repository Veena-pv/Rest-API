from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        reg = User(
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['password2']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
