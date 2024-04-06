from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Admin.models import *
from Publisher.models import *
# Create your views here.

def homepage(request):
    if 'uid' in request.session:
        return render(request,"User/HomePage.html")
    else:
        return redirect("Guest:Login")


def my_pro(request):
    if 'uid' in request.session:
        data=tbl_user.objects.get(id=request.session["uid"])
        return render(request,"User/MyProfile.html",{'data':data})
    else:
        return redirect("Guest:Login")

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
    if 'uid' in request.session:                                     
        ubookdata=tbl_genre.objects.all()
        qualitydata=tbl_quality.objects.all()
        ubook = tbl_uaddbook.objects.filter(user=request.session['uid'])

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
    else:
        return redirect("Guest:Login")



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
    if 'uid' in request.session:              
        uid = request.session['uid']
        user = tbl_user.objects.get(id=uid)
        ubook = tbl_uaddbook.objects.filter(ubook_status=0).exclude(user_id=user)
        # print(ubook.query)
        return render(request,"User/Search.html",{'data':ubook})
    else:
        return redirect("Guest:Login")

def ajaxsearch(request):
    uid = request.session['uid']
    user = tbl_user.objects.get(id=uid)
    ubook = tbl_uaddbook.objects.filter(ubook_name__istartswith=request.GET.get("bookName"),ubook_status=0).exclude(user=user)
    return render(request,"User/ajaxsearch.html",{'data':ubook})


def Viewmore(request,bid):
    if 'uid' in request.session:              
        ViewBook=tbl_uaddbook.objects.get(id=bid)
        return render(request,"User/ViewMore.html",{'ViewBook':ViewBook})
    else:
        return redirect("Guest:Login")



def Swaprequest(request,bid):
    if 'uid' in request.session:              
        uid = tbl_user.objects.get(id=request.session['uid'])
        bid=tbl_uaddbook.objects.get(id=bid)
        toUser = bid.user
        tbl_swap.objects.create( 
                touser_id=toUser,
                tobook_id=bid,
                fromuser_id=uid,
            )
        return redirect('User:Search')
    else:
        return redirect("Guest:Login")



def Viewrequest(request):
    if 'uid' in request.session:              
        uid = tbl_user.objects.get(id=request.session['uid'])
        ViewReq=tbl_swap.objects.filter(touser_id=uid,swap_paymentstatus=0)
        return render(request,"User/ViewRequest.html",{'ViewReq':ViewReq})
    else:
        return redirect("Guest:Login")


def Viewbooks(request,Fromid,sid):
    if 'uid' in request.session:              
        userFrom = tbl_user.objects.get(id=Fromid)
        ubook = tbl_uaddbook.objects.filter(user=userFrom,ubook_status=0)
        return render(request,"User/Viewbooks.html",{'data':ubook,'sid':sid})
    else:
        return redirect("Guest:Login")



def Acceptbook(request,bid,sid):
    if 'uid' in request.session:              
        swapData = tbl_swap.objects.get(id=sid)
        ubook = tbl_uaddbook.objects.get(id=bid)
        swapData.frombook_id = ubook
        swapData.save()

        frombook = tbl_uaddbook.objects.get(id=swapData.frombook_id.id)
        tobook = tbl_uaddbook.objects.get(id=swapData.tobook_id.id)
        frombook.ubook_status = 1
        tobook.ubook_status = 1
        frombook.save()
        tobook.save()

        
        if float(frombook.ubook_price) == float(tobook.ubook_price) :
            return redirect('User:Viewrequest')
        elif float(frombook.ubook_price) > float(tobook.ubook_price):
            diff = float(frombook.ubook_price) - float(tobook.ubook_price)
            return redirect('User:payment',int(diff),sid)
        else:
            diff = float(tobook.ubook_price) - float(frombook.ubook_price)
            sdata = tbl_swap.objects.get(id=sid)
            sdata.swap_price = int(diff)
            sdata.save()
            return redirect('User:Viewrequest')
    else:
        return redirect("Guest:Login")
    
def payment(request,amt,sid):
    if 'uid' in request.session:              
        if request.method == "POST":
            sdata = tbl_swap.objects.get(id=sid)
            sdata.swap_paymentstatus = 1
            sdata.swap_price = amt
            sdata.save()
            return redirect("User:homepage")
        else:
            return render(request,"User/Payment.html",{"amt":amt})
    else:
        return redirect("Guest:Login")

def mybooking(request):
    if 'uid' in request.session:              
        swap = tbl_swap.objects.filter(touser_id=request.session["uid"],swap_paymentstatus=1)
        return render(request,"User/Mybooking.html",{"swaping":swap})
    else:
        return redirect("Guest:Login")

def view_publisher_book(request):
    if 'uid' in request.session:              
        book = tbl_paddbook.objects.all()
        return render(request,"User/Publisher_book.html",{"book":book})
    else:
        return redirect("Guest:Login")


def usercomplaint(request):
    if 'uid' in request.session:              
        user_id= tbl_user.objects.get(id=request.session['uid'])

        if request.method =='POST':
            complaint_title = request.POST.get('txttitle')
            complaint_desc= request.POST.get('txtcomp')
            

            tbl_complaint.objects.create(
                
                complaint_title=complaint_title,
                complaint_desc=complaint_desc,
                user_id=user_id,
            )
            return redirect('User:homepage')
        return render(request, 'User/UserComplaint.html',{"book":user_id})
    else:
        return redirect("Guest:Login")

def Viewcomplaints(request):
    if 'uid' in request.session:              
        uid = tbl_user.objects.get(id=request.session['uid'])
        complaint=tbl_complaint.objects.filter(user_id=uid)
        return render(request,"User/Mycomplaint.html",{'complaint':complaint})
    else:
        return redirect("Guest:Login")
