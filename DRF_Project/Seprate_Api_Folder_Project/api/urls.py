from django.urls import path, include
from api.views import  EmployeeCBV
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('list', EmployeeCBV, basename='list')


urlpatterns = [
    path('', include(router.urls)),
    path('jwt-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
]