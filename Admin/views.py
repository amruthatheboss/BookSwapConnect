from django.shortcuts import render, redirect
from Admin.models import *
from Guest.models import *
from User.models import *

#Disrict DB Operations
def LoadAdminHome(request):
    return render(request,"Admin/HomePage.html")

def districtInsertSelect(request):
    district = tbl_district.objects.all()
    if request.method == 'POST':
        district = request.POST.get('txtdis')
        tbl_district.objects.create(
            district_name= district,
        )
        return redirect('webadmin:districtInsertSelect')
    return render(request, 'Admin/District.html', {'data':district})

def Districtdelete(request,id):
    district=tbl_district.objects.get(id=id).delete()
    return redirect("webadmin:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtdis")
        editdata.save()
        return redirect("webadmin:districtInsertSelect")
    else:
        return render(request,"Admin\District.html",{"editdata":editdata})
    

def Category(request):
    category = tbl_category.objects.all()
    if request.method =='POST':
        category = request.POST.get('txtcat')
        tbl_category.objects.create(
            category_name= category,
        )
        return redirect('webadmin:Category')
    return render(request, 'Admin/Category.html', {'data':category})

def Categorydelete(request,id):
    Category=tbl_category.objects.get(id=id).delete()
    return redirect('webadmin:Category')

def Categoryupdate(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editdata.category_name=request.POST.get("txtcat")
        editdata.save()
        return redirect("webadmin:Category")
    else:
        return render(request,"Admin\Category.html",{"editdata":editdata})
    



def Registration(request):
    registration = tbl_registration.objects.all()
    if request.method =='POST':
        name = request.POST.get('txtname')
        contact= request.POST.get('txtcontact')
        email= request.POST.get('txtemail')
        password=request.POST.get('txtpassword')


        tbl_registration.objects.create(
            registration_name= name,
            registration_contact=contact,
            registration_email=email,
            registration_password=password,

        )
        return redirect('webadmin:Registration')
    return render(request, 'Admin\Registration.html', {'data':registration})


def Registrationdelete(request,id):
    registration=tbl_registration.objects.get(id=id).delete()
    return redirect('webadmin:Registration')
# Create your views here.

def Registrationupdate(request,eid):
    editdata=tbl_registration.objects.get(id=eid)
    if request.method=="POST":
        editdata.registration_name=request.POST.get('txtname')
        editdata.registration_contact= request.POST.get('txtcontact')
        editdata.registration_email= request.POST.get('txtemail')
        editdata.registration_password=request.POST.get('txtpassword')
        editdata.save()
        return redirect("webadmin:Registration")
    else:
        return render(request,"Admin\Registration.html",{"editdata":editdata})
    

def Publisher(request):
    publisher = tbl_publisher.objects.all()
    if request.method =='POST':
        name = request.POST.get('txtname')
        contact= request.POST.get('txtcontact')
        email= request.POST.get('txtemail')
        address=request.POST.get('addr')


        tbl_publisher.objects.create(
            publisher_name= name,
            publisher_contact=contact,
            publisher_email=email,
            publisher_address=address,

        )
        return redirect('webadmin:Publisher')
    return render(request, 'Admin/Publisher.html', {'data':publisher})


def Publisherdelete(request,id):
    publisher=tbl_publisher.objects.get(id=id).delete()
    return redirect('webadmin:Publisher')
# Create your views here.
def Publisherupdate(request,eid):
    editdata=tbl_publisher.objects.get(id=eid)
    if request.method=="POST":
        editdata.publisher_name = request.POST.get('txtname')
        editdata.publisher_contact= request.POST.get('txtcontact')
        editdata.publisher_email= request.POST.get('txtemail')
        editdata.publisher_address=request.POST.get('addr')

        editdata.save()
        return redirect("webadmin:Publisher")
    else:
        return render(request,"Admin\Publisher.html",{"editdata":editdata})
    


def Place(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        dis=tbl_district.objects.get(id=request.POST.get('seldis'))
        tbl_place.objects.create(
            district=dis,
            place_name=request.POST.get('txtplace')
        )
        return render(request, 'Admin/Place.html',{'district':districtdata,'data':placedata}) 
    else:
        return render(request, 'Admin/Place.html',{'district':districtdata,'data':placedata}) 
    
def Subcategory(request):
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()
    if request.method=="POST":
        cat=tbl_category.objects.get(id=request.POST.get('selcat'))
        tbl_subcategory.objects.create(
            category=cat,
            subcategory_name=request.POST.get('txtsubcat')
        )
        return render(request, 'Admin/Subcategory.html',{'category':categorydata,'data':subcategorydata}) 
    else:
        return render(request, 'Admin/Subcategory.html',{'category':categorydata,'data':subcategorydata}) 
    
def Placedelete(request,id):
    place=tbl_place.objects.get(id=id).delete()
    return redirect('webadmin:Place')

def Subcategorydelete(request,id):
    subcategory=tbl_subcategory.objects.get(id=id).delete()
    return redirect('webadmin:Subcategory')

def Genre(request):
    genre = tbl_genre.objects.all()
    if request.method =='POST':
        g_name = request.POST.get('genre_name')

        tbl_genre.objects.create(
            gen_name=g_name,
        )
        return redirect('webadmin:Genre')
    return render(request, 'Admin/Genre.html', {'data':genre})

def Genredelete(request,id):
    genre_del=tbl_genre.objects.get(id=id).delete()
    return redirect("webadmin:Genre")

def Genreupdate(request,eid):
    editdata=tbl_genre.objects.get(id=eid)
    if request.method=="POST":
        editdata.gen_name=request.POST.get("genre_name")
        editdata.save()
        return redirect("webadmin:Genre")
    else:
        return render(request,"Admin\Genre.html",{"editdata":editdata})
    

def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Admin/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("webadmin:LoadAdminHome")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("webadmin:LoadAdminHome")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Admin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserListRejected.html",{"userdata":userdata})

def publisherListNew(request):
    userdata = tbl_publisher.objects.filter(user_status=0)
    for i in userdata:
        print(i.publisher_name)
    return render(request,"Admin/PublisherListNew.html",{"userdata":userdata})

def acceptpub(request,aid):
    user = tbl_publisher.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("webadmin:LoadAdminHome")

def rejectpub(request,rid):
    user = tbl_publisher.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("webadmin:LoadAdminHome")

def publisherListAccepted(request):
    userdata = tbl_publisher.objects.filter(user_status=1)
    return render(request,"Admin/PublisherListAccepted.html",{"userdata":userdata})

def publisherListRejected(request):
    userdata = tbl_publisher.objects.filter(user_status=2)
    return render(request,"Admin/PublisherListRejected.html",{"userdata":userdata})

def agentListNew(request):
    userdata= tbl_agent.objects.filter(user_status=0)
    return render(request,"Admin/AgentListNew.html",{"userdata":userdata})

def acceptagent(request,aid):
    user = tbl_agent.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("webadmin:LoadAdminHome")

def rejectagent(request,rid):
    user = tbl_agent.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("webadmin:LoadAdminHome")

def agentListAccepted(request):
    userdata = tbl_agent.objects.filter(user_status=1)
    return render(request,"Admin/AgentListAccepted.html",{"userdata":userdata})

def agentListRejected(request):
    userdata = tbl_agent.objects.filter(user_status=2)
    return render(request,"Admin/AgentListRejected.html",{"userdata":userdata})

def Quality(request):
    quality = tbl_quality.objects.all()
    if request.method =='POST':
        level = request.POST.get('txtqlt')
        rule=request.POST.get('txtrule')
        percentage=request.POST.get('txtpercentage')

        tbl_quality.objects.create(
            quality_level = level,
            quality_rule = rule,
            quality_percentage = percentage,

        )
        return redirect('webadmin:Quality')
    return render(request, 'Admin/Quality.html', {'data':quality})


def Qualitydelete(request,id):
    quality=tbl_quality.objects.get(id=id).delete()
    return redirect('webadmin:Quality')

def Qualityupdate(request,eid):
    editdata=tbl_quality.objects.get(id=eid)
    if request.method=="POST":
        editdata.quality_level = request.POST.get('txtqlt')
        editdata.quality_rule = request.POST.get('txtrule')
        editdata.quality_percentage = request.POST.get('txtpercentage')

        editdata.save()
        return redirect("webadmin:Quality")
    else:
        return render(request,"Admin\Quality.html",{"editdata":editdata})
    
def vieworders(request):
    swap = tbl_swap.objects.all()
    return render(request,"Admin/View_orders.html",{"swaping":swap})

def completed(request,id):
    swap = tbl_swap.objects.get(id=id)
    swap.swap_status = 6
    swap.save()
    return redirect("webadmin:vieworders")

def viewcomplaint(request):
    userdata=tbl_user.objects.all()
    publisherdata=tbl_publisher.objects.all()
    usercomplaint=tbl_complaint.objects.filter(user_id__in=userdata)
    publishercomplaint=tbl_complaint.objects.filter(publisher_id__in=publisherdata)
    
    return render(request,"Admin/Viewcomplaint.html",{'usercomplaint':usercomplaint,'publishercomplaint':publishercomplaint})

def reply(request,id):
    data= tbl_complaint.objects.get(id=id)
    if request.method == 'POST':
        reply = request.POST.get('txtreply')
        data.complaint_reply=reply
        data.complaint_status=1
        data.save()
        
        return redirect('webadmin:viewcomplaint')
    else:
        return render(request, 'Admin/Reply.html', {'data':data})