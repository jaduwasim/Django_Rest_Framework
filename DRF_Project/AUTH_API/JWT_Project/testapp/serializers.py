from rest_framework import serializers
from .models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# from rest_framework.views import APIView
# from rest_framework.viewsets import ViewSet
# from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
# from django.db.models import Q, Avg, Min, Max, Sum, Count
# from django.contrib.auth.models import User
# from django.core.serializers import serialize
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.forms import Form, ModelForm
# from rest_framework.serializers import Serializer, ModelSerializer
# from django.db.models import Model
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from rest_framework.renderers import JSONRenderer
# from io import BytesIO
# from rest_framework.parsers import JSONParser
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from rest_framework_simplejwt.authentication import JWTAuthentication


# DJANGO:
# ------

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include
from django.db.models import Model
from django.forms import Form, ModelForm
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView