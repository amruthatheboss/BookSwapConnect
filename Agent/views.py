from django.shortcuts import render
from Guest.models import *
# Create your views here.

def homepage(request):
    return render(request,"Agent/HomePage.html")

def my_pro(request):
    data=tbl_agent.objects.get(id=request.session["sid"])
    return render(request,"Agent/MyProfile.html",{'data':data})


def editprofile(request):
    prodata=tbl_agent.objects.get(id=request.session["sid"])
    if request.method=="POST":
        prodata.agent_name=request.POST.get('txtname')
        prodata.agent_contact=request.POST.get('txtcon')
        prodata.agent_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Agent/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Agent/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_agent.objects.filter(id=request.session["sid"],agent_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                agentdata=tbl_agent.objects.get(id=request.session["sid"],agent_password=request.POST.get('txtcurpass'))
                agentdata.agent_password=request.POST.get('txtnewpass')
                agentdata.save()
                return render(request,"Agent/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Agent/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Agent/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Agent/ChangePassword.html")
