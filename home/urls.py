from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index , name = 'home'),
    path('college/',include('college.urls')),
    path('govt/',include('govt.urls')),
    path('student/',include('student.urls')),
    path('api/',include('college.api_urls'))
]
