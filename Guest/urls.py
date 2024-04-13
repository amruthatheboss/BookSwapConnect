from django.urls import path
from Guest import views

app_name = "Guest"

urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('Publisher/',views.Publisher, name='Publisher'),
    path('Agent/',views.Agent, name='Agent'),
    path('Login/',views.Login,name="Login"),
    path('',views.Home,name="Home"),



]
    