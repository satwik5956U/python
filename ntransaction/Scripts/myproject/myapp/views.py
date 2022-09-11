from email import message
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from . import models

# Create your views here.
def index(request):
    return render(request,'login.html')
def signup(request):
    
    return render(request,'signup.html')
def signin(request):
    return render(request,'signin.html')
def signupdata(request):
    d=models.Members.objects.all()
    for i in d:
        if i.acc==request.GET['accnum'] and i.passw==request.GET['pass']:
            return HttpResponse("already registered")
    m=models.Members(fname=request.GET['na'],lname=request.GET['lna'],acc=request.GET['accnum'], amt=0.00,date=str(dt.datetime.now()),passw=request.GET['pass'])
    m.save()
    return HttpResponse("registered successfully")
def signindata(request):
    e=models.Members.objects.all()
    for i in e:
        if  (i.acc==request.GET['baccno'] and i.passw==request.GET['pass']):
            return render(request,'signinacc.html',{'acc':i.acc,'passw':i.passw})
        return HttpResponse("incorrect")
    
def creditbutton(request):
    return HttpResponse(request.GET['acc'])