from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.


def Home(request):
    return render(request,"Guest/Home.html")



def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place,user_address=request.POST.get("txt_address"))
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})

def ajaxplace(request):
    if request.GET.get("did")!= "":
        dis = tbl_district.objects.get(id=request.GET.get("did"))
        place = tbl_place.objects.filter(district=dis)
        return render(request,"Guest/AjaxPlace.html",{"placedata":place})
    else:
        return render(request,"Guest/AjaxPlace.html")
    
def Publisher(request):
    publisher = tbl_publisher.objects.all()
    if request.method =='POST':
        name = request.POST.get('txtname')
        contact= request.POST.get('txtcontact')
        address=request.POST.get('txtadd')
        photo=request.FILES.get('photo')
        proof=request.FILES.get('proof')
        email= request.POST.get('txtemail')
        password=request.POST.get('txtpassword')


        tbl_publisher.objects.create(
            publisher_name= name,
            publisher_contact=contact,
            publisher_address= address,
            publisher_photo= photo,
            publisher_proof= proof,
            publisher_email=email,
            publisher_password=password,

        )
        return redirect('Guest:Publisher')
    return render(request, 'Guest/Publisher.html', {'data':publisher})

def Agent(request):
    agent = tbl_agent.objects.all()
    if request.method =='POST':
        name = request.POST.get('txtname')
        contact= request.POST.get('txtcontact')
        address=request.POST.get('txtadd')
        photo=request.FILES.get('photo')
        proof=request.FILES.get('proof')
        email= request.POST.get('txtemail')
        password=request.POST.get('txtpassword')


        tbl_agent.objects.create(
            agent_name= name,
            agent_contact=contact,
            agent_address= address,
            agent_photo= photo,
            agent_proof= proof,
            agent_email=email,
            agent_password=password,

        )
        return redirect('Guest:Agent')
    return render(request, 'Guest/Agent.html', {'data':agent})
    
def Login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        publishercount = tbl_publisher.objects.filter(publisher_email=request.POST.get("txt_email"),publisher_password=request.POST.get("txt_password"),user_status = 1).count()
        agentcount = tbl_agent.objects.filter(agent_email=request.POST.get("txt_email"),agent_password=request.POST.get("txt_password"),user_status = 1).count()
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:homepage")
        
        elif publishercount > 0:
            publisher = tbl_publisher.objects.get(publisher_email=request.POST.get("txt_email"),publisher_password=request.POST.get("txt_password"))
            request.session["pid"] = publisher.id
            request.session["uname"] = publisher.publisher_name
            return redirect("Publisher:homepage")
        
        elif agentcount > 0:
            agent = tbl_agent.objects.get(agent_email=request.POST.get("txt_email"),agent_password=request.POST.get("txt_password"))
            request.session["sid"] = agent.id
            request.session["uname"] = agent.agent_name
            return redirect("Agent:homepage")
        
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("webadmin:LoadAdminHome")

        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")