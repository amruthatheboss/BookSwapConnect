from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Publisher.models import *
# Create your views here.

def homepage(request):
    return render(request,"Publisher/HomePage.html")

def my_pro(request):
    data=tbl_publisher.objects.get(id=request.session["pid"])
    return render(request,"Publisher/MyProfile.html",{'data':data})

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
    pbookdata=tbl_genre.objects.all()
    pbook = tbl_paddbook.objects.all()
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
        )
        return redirect('Publisher:PublisherAddBook')
    return render(request, 'Publisher/PublisherAddBook.html',{'genre':pbookdata,'data':pbook})


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


