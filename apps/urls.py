from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TodoViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
