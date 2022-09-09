from django.shortcuts import render
from rest_framework.generics import (CreateAPIView,RetrieveDestroyAPIView, 
                                    RetrieveUpdateDestroyAPIView, ListAPIView,
                                    RetrieveAPIView)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from quiz.models import Test
from quiz.serializers import TestSerializer


class CreateTestView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdminUser]

class UpdateDestroyTestView(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdminUser,]

class ListTestView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny,]

class GetTestView(RetrieveAPIView):
    ueryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny,]




