from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
import pandas as pd 
from .models import College
import uuid 


# Create your views here
def Register(request):
    register_objs = Registers.objects.all()
    serializer = RegistersSerializer(register_objs, many=True)
    df = pd.DataFrame(serializer.data)
    df.to_csv(f"/var/www/studentpeeps/media/data{uuid.uuid4()}.csv", encoding="UTF-8", index=False)
    return HttpResponse("Data Printed")


def Uploads(request):
    Uploads_objs = Upload.objects.all()
    serializer = UploadsSerializer(Uploads_objs, many=True)
    df = pd.DataFrame(serializer.data)
    df.to_csv(f"/var/www/studentpeeps/media/data{uuid.uuid4()}.csv", encoding="UTF-8", index=False)
    return HttpResponse("Data Printed")


def error_404_view(request, exception):
     return render(request, '404.html')


def SignUpView(request):
    return render(request, 'signupview.html', {'Institution': Institution})
	