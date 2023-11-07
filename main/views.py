from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import InstructorSerializer
from .import models
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication


# Create your views here.
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

class InstructorList(generics.ListCreateAPIView):
        queryset = models.Instructor.objects.all()
        serializer_class = InstructorSerializer
        permission_classes = [IsAuthenticated] 

class InstructorDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = models.Instructor.objects.all()
        serializer_class = InstructorSerializer
        permission_classes = [IsAuthenticated]
        
        
