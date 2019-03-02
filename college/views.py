from django.shortcuts import render
from django.http import HttpResponse
from .models import cdata
from .models import validated
from student.models import sdata
from rest_framework import viewsets
from .serializers import validatedserializer

def index(request):
    return render(request , 'college/login.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    if( (username == "collegeadmin") and (password == "pass@123")):
        return render(request , 'college/auth.html')
    else:
        return render(request , 'college/accessdenied.html')

def display(request):
    data_set = sdata.objects.all()
    context = {
        'data_set' : data_set
    }
    return render(request , 'college/data_set.html', context)


def check(request):
    data_set = sdata.objects.all()
    validate_set = validated.objects.all()
    college_data = cdata.objects.all()
    selected = data_set.get(sap = request.POST['student'])
    print(selected.sap)
    # if selected in validate_set:
    #     print(selected.name)
    try:
        x = college_data.get(sap = selected.sap)
        print("Data Fetched From Colege Db")
        context = {
            'data_set' : data_set,
            'validate_set' : validate_set
        }
        daydiff = (selected.issued - x.previssued)%30
        monthdiff = ((selected.issuem - x.previssuem)%12)*30
        validcount = int(daydiff)+int(monthdiff)
        if((x.source == selected.source) and (validcount>=120) and (x.name == selected.name) and (x.dept == selected.dept ) and (x.sap == selected.sap) and (selected.destination == 'Vile-Parle')):
            obj = validated(name = selected.name , source = selected.source , type = selected.type , destination = "Vile-Parle")
        #if (validate_set.get(name = x.name) == '\0'):
            obj.save()
            selected.delete()
            return render(request ,'college/data_set.html', context)
            #return HttpResponse("<em>Done!</em>")
        else:
            #return HttpResponse("<em>Already validated</em>")
            return(request , 'college/data_set.html', context)
    except:
        selected.delete()
        return HttpResponse("<em>No Such Student!</em>")

class validatedViewSet(viewsets.ModelViewSet):
    queryset = validated.objects.all()
    serializer_class = validatedserializer
