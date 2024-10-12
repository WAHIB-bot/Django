from rest_framework import serializers
from .models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']

    def create(self,validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user        