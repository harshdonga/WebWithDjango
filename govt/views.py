from django.shortcuts import render
from django.http import HttpResponse
from .models import auth
import requests

def index(request):
    return render(request , 'govt/login.html')

def check(request):
    username = request.POST['username']
    password = request.POST['password']
    data_set = auth.objects.all()
    try:
        user = data_set.get(username = username)
        print(user)
        if( password == user.password):
            print(user.password)
            url = 'http://127.0.0.1:8000/api/college/'
            r = requests.get(url).json()
            print(r)
            return render(request , 'govt/auth.html' ,{ 'user' : user , 'r': r})
        else:
            return render(request , 'govt/accessdenied.html')
    except:
        return render(request , 'govt/accessdenied.html')


def add(request):
    name = request.POST['rail']
    print(name)
    return HttpResponse()
