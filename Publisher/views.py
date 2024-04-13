from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Publisher.models import *
from User.models import *
# Create your views here.

def homepage(request):
    if 'pid' in request.session:
        return render(request,"Publisher/HomePage.html")
    else:
        return redirect("Guest:Login")

def my_pro(request):
    if 'pid' in request.session:
        data=tbl_publisher.objects.get(id=request.session["pid"])
        return render(request,"Publisher/MyProfile.html",{'data':data})
    else:
        return redirect("Guest:Login")

def editprofile(request):
    prodata=tbl_publisher.objects.get(id=request.session["pid"])
    if request.method=="POST":
        prodata.publisher_name=request.POST.get('txtname')
        prodata.publisher_contact=request.POST.get('txtcon')
        prodata.publisher_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Publisher/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Publisher/EditProfile.html",{'prodata':prodata})
   
def changepassword(request):
    if request.method=="POST":
        ccount=tbl_publisher.objects.filter(id=request.session["pid"],publisher_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                publisherdata=tbl_publisher.objects.get(id=request.session["pid"],publisher_password=request.POST.get('txtcurpass'))
                publisherdata.publisher_password=request.POST.get('txtnewpass')
                publisherdata.save()
                return render(request,"Publisher/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Publisher/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Publisher/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Publisher/ChangePassword.html")
        
def PublisherAddBook(request):   
    if 'pid' in request.session:                                       
        pbookdata=tbl_genre.objects.all()
        pbook = tbl_paddbook.objects.filter(publisher=request.session['pid'])
        if request.method =='POST':
            pgen=tbl_genre.objects.get(id=request.POST.get('selgenre'))
            pname = request.POST.get('txtname')
            pdesc= request.POST.get('txtdesc')
            pprice= request.POST.get('txtprice')
            pphoto=request.FILES.get('photo')
            pauthname= request.POST.get('txtaname')
            pqty=request.POST.get('txtqty')


            tbl_paddbook.objects.create(
                
                pbook_name=pname,
                pbook_desc=pdesc,
                pbook_price=pprice,
                pbook_photo=pphoto,
                pbook_authname=pauthname,
                pbook_genre=pgen,
                pbook_qty=pqty,
                publisher=tbl_publisher.objects.get(id=request.session['pid'])
            )
            return redirect('Publisher:PublisherAddBook')
        return render(request, 'Publisher/PublisherAddBook.html',{'genre':pbookdata,'data':pbook})
    else:
        return redirect("Guest:Login")


def PublisherBookdelete(request,id):
    pbook=tbl_paddbook.objects.get(id=id).delete()
    return redirect('Publisher:PublisherAddBook')
# Create your views here.
def PublisherBookupdate(request,eid):
    pbookdata=tbl_genre.objects.all()
    editdata=tbl_paddbook.objects.get(id=eid)
    if request.method=="POST":
        editdata.pbook_name = request.POST.get('txtname')
        editdata.pbook_desc= request.POST.get('txtdesc')
        editdata.pbook_price= request.POST.get('txtprice')
        editdata.pbook_photo=request.FILES.get('photo')
        editdata.pbook_authname= request.POST.get('txtaname')
        editdata.pbook_genre=tbl_genre.objects.get(id=request.POST.get('selgenre'))
        editdata.pbook_qty=request.POST.get('txtqty')


        editdata.save()
        return redirect("Publisher:PublisherAddBook")
    else:
            return render(request,"Publisher\PublisherAddBook.html",{"editdata":editdata,'genre':pbookdata})


def publishercomplaint(request):
    if 'pid' in request.session:          
        publisher_id= tbl_publisher.objects.get(id=request.session['pid'])

        if request.method =='POST':
            complaint_title = request.POST.get('txttitle')
            complaint_desc= request.POST.get('txtcomp')
            

            tbl_complaint.objects.create(
                
                complaint_title=complaint_title,
                complaint_desc=complaint_desc,
                publisher_id=publisher_id,
            )
            return redirect('Publisher:homepage')
        return render(request, 'Publisher/Publishercomplaint.html',{"book":publisher_id})
    else:
        return redirect("Guest:Login")
    


def Viewpublishercomplaints(request):
    if 'pid' in request.session:      
        pid = tbl_publisher.objects.get(id=request.session['pid'])
        complaint=tbl_complaint.objects.filter(publisher_id=pid)
        return render(request,'Publisher/Viewpcomplaint.html',{'complaint':complaint})
    else:
        return redirect("Guest:Login")

def logout(request):
    del request.session['pid']
    return redirect("Guest:Login")


