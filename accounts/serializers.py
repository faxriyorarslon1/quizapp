from rest_framework import serializers,validators
from .models import User
# from django.contrib.auth.models import User

# from accounts.models import User

class RegisterSerializer(serializers.ModelSerializer):
  # password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

  class Meta:
    model = User
    fields = ['phone','fullname','password']
    extra_kwargs = {
        'password': {'write_only':True}
    }

def save(self):
  account = User(
            phone=self.validated_data['phone'],
            fullname=self.validated_data['fullname'],
  )
  password = self.validated_data['password']
  # password2 = self.validated_data['password2']

  # if password != password2:
  #   raise serializers.ValidationError({'password': 'Passwords must match.'})
  account.set_password(password)
  account.save()
  return account

def create(self,validated_data):
    phone = validated_data.get('phone')
    password = validated_data.get('password')
    fullname = validated_data.get('fullname')

    user = User.objects.create(
      phone=phone,
      password=password,
      fullname=fullname
    )
    return user

