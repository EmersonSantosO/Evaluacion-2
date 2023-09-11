from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignUpViewSet, ProfileUpdateViewSet

router = DefaultRouter()
router.register(r'signup', SignUpViewSet, basename='signup')
router.register(r'profile', ProfileUpdateViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
