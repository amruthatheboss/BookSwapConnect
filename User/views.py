from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Admin.models import *
# Create your views here.

def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})


def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")
    

def UserAddBook(request):                                          
    ubookdata=tbl_genre.objects.all()
    qualitydata=tbl_quality.objects.all()
    ubook = tbl_uaddbook.objects.all()

    if request.method =='POST':
        user = tbl_user.objects.get(id=request.session['uid'])
        ugen=tbl_genre.objects.get(id=request.POST.get('selgenre'))
        uqlty=tbl_quality.objects.get(id=request.POST.get('selquality'))
        uname = request.POST.get('txtname')
        udesc= request.POST.get('txtdesc')
        uprice= request.POST.get('txtprice')
        uphoto=request.FILES.get('photo')
        uauthname= request.POST.get('txtaname')
        qltprice=(float(uqlty.quality_percentage)/100)*float(uprice)
        


        tbl_uaddbook.objects.create(
            
            ubook_name=uname,
            ubook_desc=udesc,
            ubook_price=qltprice,
            ubook_photo=uphoto,
            ubook_authname=uauthname,
            ubook_genre=ugen,
            ubook_qlty=uqlty,
            user=user,
        )
        return redirect('User:UserAddBook')
    return render(request, 'User/UserAddBook.html',{'quality':qualitydata,'genre':ubookdata, 'data':ubook})


def UserBookDelete(request,id):
    ubook=tbl_uaddbook.objects.get(id=id).delete()
    return redirect('User:UserAddBook')
# Create your views here.
def UserBookupdate(request,eid):
    ubookdata=tbl_genre.objects.all()
    qualitydata=tbl_quality.objects.all()
    editdata=tbl_uaddbook.objects.get(id=eid)
    if request.method=="POST":
        editdata.ubook_name = request.POST.get('txtname')
        editdata.ubook_desc= request.POST.get('txtdesc')
        uqlty=tbl_quality.objects.get(id=request.POST.get('selquality'))
        uprice = request.POST.get('txtprice')
        editdata.ubook_price= (float(uqlty.quality_percentage)/100)*float(uprice)
        editdata.ubook_photo=request.FILES.get('photo')
        editdata.ubook_authname= request.POST.get('txtaname')
        editdata.ubook_genre=tbl_genre.objects.get(id=request.POST.get('selgenre'))
        editdata.ubook_qlty=tbl_quality.objects.get(id=request.POST.get('selquality'))
        

        editdata.save()
        return redirect("User:UserAddBook")
    else:
            return render(request,"User/UserAddBook.html",{"editdata":editdata,'genre':ubookdata,'quality':qualitydata})


def searchbook(request):
    uid = request.session['uid']
    user = tbl_user.objects.get(id=uid)
    ubook = tbl_uaddbook.objects.filter().exclude(user=user)
    return render(request,"User/Search.html",{'data':ubook})


def ajaxsearch(request):
    uid = request.session['uid']
    user = tbl_user.objects.get(id=uid)
    ubook = tbl_uaddbook.objects.filter(ubook_name__istartswith=request.GET.get("bookName")).exclude(user=user)
    return render(request,"User/ajaxsearch.html",{'data':ubook})


def Viewmore(request,bid):
    ViewBook=tbl_uaddbook.objects.get(id=bid)
    return render(request,"User/ViewMore.html",{'ViewBook':ViewBook})



def Swaprequest(request,bid):
    uid = tbl_user.objects.get(id=request.session['uid'])
    bid=tbl_uaddbook.objects.get(id=bid)
    toUser = bid.user
    tbl_swap.objects.create( 
            touser_id=toUser,
            tobook_id=bid,
            fromuser_id=uid,
        )
    return redirect('User:Search')



def Viewrequest(request):
    uid = tbl_user.objects.get(id=request.session['uid'])
    ViewReq=tbl_swap.objects.filter(touser_id=uid)
    return render(request,"User/ViewRequest.html",{'ViewReq':ViewReq})


def Viewbooks(request,Fromid):
    userFrom = tbl_user.objects.get(id=Fromid)
    ubook = tbl_uaddbook.objects.filter(user=userFrom)
    return render(request,"User/Viewbooks.html",{'data':ubook})