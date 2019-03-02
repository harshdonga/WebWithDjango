from django.urls import path , include
from .import views

urlpatterns = [
    path('',views.index , name = 'collegehome'),
    path('login/', views.login , name = 'login'),
    path('display/', views.display , name = 'display'),
    path('check/' , views.check , name = 'check')
]
