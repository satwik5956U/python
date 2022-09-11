from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signupdata',views.signupdata,name="signupdata"),
    path('signindata',views.signindata,name="signindata"),
    path('creditbutton',views.creditbutton,name="creditbutton"),
]
