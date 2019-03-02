from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index , name = 'govthome'),
    path('check/', views.check , name = 'check'),
]
