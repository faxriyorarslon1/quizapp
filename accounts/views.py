from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.serializers import RegisterSerializer
# from accounts.serializers import RegistrationSerializer

# @api_view(['POST',])
# def registration_view(request):
#   if request.method == 'POST':
#     serializer = RegistrationSerializer(data=request.data)
#     data = {}
#     if serializer.is_valid():
#       account = serializer.save()
#       data['response'] = "Successfully registred a new user."
#       data['phone'] = account.phone
#       data['fullname'] = account.fullname

#     else:
#       data = serializer.errors
#     return Response(data)

@api_view(['POST'])
def login_api(request):
  serializer = AuthTokenSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  user = serializer.validated_data['user']
  _, token = AuthToken.objects.create(user)

  return Response({
      'user_info':{
        'id':user.id,
        'phone':user.phone,
        'fullname':user.fullname
        },
      'token':token
  })

@api_view(['GET'])
def get_user_data(request):
  user = request.user

  if user.is_authenticated:
    return Response({
        'user_info':{
          'id':user.id,
          'phone':user.phone,
          'fullname':user.fullname
        },
    })
  return Response({'error':'not authenticated'},status=400)

@api_view(['POST'])
def register_api(request):
  serializer = RegisterSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)

  user = serializer.save()
  _, token = AuthToken.objects.create(user)

  return Response({
      'user_info':{
        'id':user.id,
        'phone':user.phone,
        'fullname':user.fullname
        },
      'token':token
  })









