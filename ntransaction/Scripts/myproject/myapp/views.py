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
    global accnum,passwo,amnt,finame,laname
    for i in e:
        if  (i.acc==request.GET['baccno'] and i.passw==request.GET['pass']):
            accnum=i.acc
            passwo=i.passw
            amnt=i.amt
            finame=i.fname
            laname=i.lname
            return render(request,'signinacc.html',{'acc':i.acc,'passw':i.passw})
    return HttpResponse("incorrect")
    
def creditbutton(request):
    return render(request,'creditpage.html')
def creditpage(request):
    #amnt=float(amnt)+float(request.GET['creamt'])
    m=models.Members.objects.filter(acc=accnum,passw=passwo)
    mid=0
    for i in m:
        if i.id>mid:
            n=i.amt
    m=models.Members(fname=finame,lname=laname,acc=accnum,amt=n+int(request.GET['creamt']),date=str(dt.datetime.now()))
    m.save()
    return HttpResponse(str(n))
def ministate(request):
    m=models.Members.objects.filter(acc=accnum,passw=passwo)
    context={
        'mydata':m
    }
    return render(request,'ministate.html',context)