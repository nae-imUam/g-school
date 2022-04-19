from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Teacher, OtherStaff, School, Student

Schoolid = 0
teacherid = 0
stuid = 0
empid = 0

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
    #be_a_passenger(user.first_name, user.last_name)
    jobType = request.POST["jobType"]


    if jobType == "Teacher" or jobType == "HeadMaster":
        try:
            teacher = Teacher( int(username), int(username), first_name+last_name)
            teacher.save()
            user.save()
            login(request, user)
            return render(request, "Teachers/index.html", teacher)
        except:
            return HttpResponseRedirect(reverse("index"))
    if jobType == "Other Staff":
        try:
            staff = OtherStaff( int(user.username), first_name+last_name)
            staff.save()
            user.save()
            login(request, user)
            return render(request, "NTStaffs/index.html", teacher)
        except:
            return HttpResponseRedirect(reverse("index"))


def add_new_form(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})

    return render(request, "flights/addnew.html")

def add_new(request, user):
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


def update_profile(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    jobType = request.POST["jobType"]
    first_name = request.POST["user_first_name"]
    last_name = request.POST["user_last_name"]
    user.first_name = first_name
    user.last_name = last_name
    if first_name == "" or last_name == "" or jobType == "":
        context = {
            "user": request.user
        }
        return render(request, "users/update_profile.html", context)

    if jobType == "Teacher" or jobType == "HeadMaster":
        teacher = Teacher('', teacherid, '', first_name+lastmane, '')
        teacherid = teacherid + 1
        teacher.save()
        return render(request, "Teachers/index.html", teacher)

    if jobType == "Other Staff":
        staff = OtherStaff('', empid, '', first_name+lastmane, '')
        empid = empid + 1
        staff.save()
        return render(request, "NTStaffs/index.html", teacher)
