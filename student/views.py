from django.shortcuts import render
from django.http import HttpResponse
from .models import sdata

def index(request):
    return render(request , 'student/submissionform.html' , {} )

def add_sdata(request):
    name   = request.POST["name"]
    sap    = request.POST["sap"]
    source = request.POST["source"]
    issued = request.POST["issued"]
    issuem = request.POST["issuem"]
    dept = request.POST["dept"]
    type = request.POST["type"]
    destination = request.POST["destination"]

    studentdata = sdata(name = name , sap = sap, source = source , issued = issued , issuem = issuem , dept = dept , destination = destination , type = type)
    studentdata.save()

    return render(request ,'student/thanks.html', { 'name' : name })
