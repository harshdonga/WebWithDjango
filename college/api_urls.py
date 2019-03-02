from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('' , validatedViewSet)

urlpatterns = [
    path('college/' , include(router.urls)),
]
