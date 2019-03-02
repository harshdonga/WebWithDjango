from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index , name = 'studenthome'),
    path('add_sdata/',views.add_sdata , name = 'add_sdata')
]
