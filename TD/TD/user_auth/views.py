from http.client import HTTPResponse
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return HttpResponse('ikkada nundi ni pani mava')
def login_view(request):
    logout(request)
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponse('ikkada nundi ni pani mava')
        # Otherwise, return login page again with new context
        else:
            return render(request, "user_auth/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "user_auth/login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        User.objects.create_user(username, email, password)
        return HttpResponseRedirect(reverse("login"))

    return render(request, "user_auth/signup.html")
