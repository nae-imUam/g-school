from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        #"flights": Flight.objects.all(),
        "user": request.user
    }
    return render(request, "base/index.html", context)
'''
def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'Users/signup.html')
'''


def addschoolform(request):
    return render(request, 'base/addschool.html')

def addschool(request):
    return 'hello'


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def signup_view(request):
    return render(request, "users/signup.html")


def create_new_user(request):
    username = request.POST["username"]
    first_name = request.POST["user_first_name"]
    last_name = request.POST["user_last_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    user = User.objects.create_user(username, email, password)
    #user.first_name = username
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    #be_a_passenger(user.first_name, user.last_name)
    login(request, user)
    return HttpResponseRedirect(reverse("index"))

def add_new_form(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})

    return render(request, "flights/addnew.html")

def add_new(request, ):
    if not request.user.is_authenticated:
        return render(request, "Users/login.html", {"message": None})

    #try:
    #    flight = Flight.objects.get(pk=flight_id)
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    #except Flight.DoesNOtExist:
    #    return render(request, "flights/error.html", {"message": "No Flight."})
    #add a new passenger.
    #be_a_passenger(first_name, last_name)
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
