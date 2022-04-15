from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("new_user", views.create_new_user, name="new_user"),
    path("add_new", views.add_new, name="add_new"),
    path("add_new_form", views.add_new_form, name="add_new_form"),
]
