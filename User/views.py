from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Admin.models import *
from Publisher.models import *
from django.http import JsonResponse
# Create your views here.

def homepage(request):
    if 'uid' in request.session:
        uid = request.session['uid']
        user = tbl_user.objects.get(id=uid)
        # ubook = tbl_uaddbook.objects.filter(ubook_status=0).exclude(user=user)
        user_genre = tbl_usergenre.objects.filter(user=user).values_list('genre', flat=True) 
        ubook = tbl_uaddbook.objects.filter(ubook_status=0, ubook_genre__in=user_genre).exclude(user_id=user)
       
        return render(request,"User/HomePage.html",{'ubook':ubook})
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
        ubook = tbl_uaddbook.objects.filter(user=request.session['uid'],ubook_status=0)

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
            sdata.swap_paymentstatus = -1
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
        user = tbl_user.objects.get(id=request.session["uid"])
        swap = tbl_swap.objects.filter(touser_id=request.session["uid"],swap_paymentstatus__lte=1)
        swapfrom = tbl_swap.objects.filter(fromuser_id=request.session["uid"],swap_paymentstatus__lte=1)
        return render(request,"User/Mybooking.html",{"swaping":swap,"user":user,"fromuser":swapfrom})
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
    

def searchpbook(request):
    if 'uid' in request.session:    
        ar=[1,2,3,4,5]
        parry=[]
        avg=0          
        pbook = tbl_paddbook.objects.all()
        # print(ubook.query)
        for i in pbook:
            wdata=tbl_paddbook.objects.get(id=i.id)
            tot=0
            ratecount=tbl_rating.objects.filter(book=wdata).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(book=wdata)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(pbook,parry)
        return render(request,"User/searchp.html",{'data':datas,"ar":ar})
    else:
        return redirect("Guest:Login")

def ajaxpsearch(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0 
    pbook = tbl_paddbook.objects.filter(pbook_name__istartswith=request.GET.get("bookName"))
    for i in pbook:
        wdata=tbl_paddbook.objects.get(id=i.id)
        tot=0
        ratecount=tbl_rating.objects.filter(book=wdata).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(book=wdata)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(pbook,parry)
    return render(request,"User/ajaxpsearch.html",{'data':datas,"ar":ar})

def ViewPmore(request,bid):
    if 'uid' in request.session:              
        ViewBook=tbl_paddbook.objects.get(id=bid)
        return render(request,"User/ViewPmore.html",{'ViewBook':ViewBook})
    else:
        return redirect("Guest:Login")

def Addcart(request,pid):
    if 'uid' in request.session:  
        productdata=tbl_paddbook.objects.get(id=pid)
        custdata=tbl_user.objects.get(id=request.session["uid"])
        bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"User/searchp.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
                return redirect("User:searchpbook")
        else:
            tbl_booking.objects.create(user=custdata)
            bookingcount=tbl_booking.objects.filter(booking_status=0,user=custdata).count()
            if bookingcount>0:
                bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
                cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
                if cartcount>0:
                    msg="Already added"
                    return render(request,"User/searchp.html",{'msg':msg})
                else:
                    tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
                    return redirect("User:searchpbook")
    else:
        return redirect("Guest:Login")
    
def Mycart(request):
   if request.method=="POST":
    bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
    bookingdata.booking_amount=request.POST.get("carttotalamt")
    bookingdata.booking_status=1
    bookingdata.save()
    return redirect("User:cartpayment")
   else:
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
    #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
    if bcount>0:
        #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
        book=tbl_booking.objects.get(user=customerdata,booking_status=0)
        bid=book.id
        request.session["bookingid"]=bid
        bkid=tbl_booking.objects.get(id=bid)
        cartdata=tbl_cart.objects.filter(booking=bkid)
        return render(request,"User/MyCart.html",{'data':cartdata})
    else:
        return render(request,"User/MyCart.html")

def DelCart(request,did):
    tbl_cart.objects.get(id=did).delete()
    return redirect("User:Mycart")

def CartQty(request):
    qty=request.GET.get('QTY')
    cartid=request.GET.get('ALT')
    cartdata=tbl_cart.objects.get(id=cartid)
    cartdata.cart_qty=qty
    cartdata.save()
    return redirect("User:Mycart")

def cartpayment(request):
    bk = tbl_booking.objects.get(id=request.session["bookingid"])
    if request.method == "POST":
        cart = tbl_cart.objects.filter(booking=request.session["bookingid"])
        bk.booking_status = 2
        bk.save()
        for i in cart:
            pdt = tbl_paddbook.objects.get(id=i.product_id )
            stock = pdt.pbook_qty
            qty = i.cart_qty
            bal = int(stock) - int(qty)
            pdt.pbook_qty = bal
            pdt.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"amts":bk})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def mypdtbooking(request):
    bk = tbl_booking.objects.filter(user=request.session["uid"],booking_status=2)
    return render(request,"User/My_Booking.html",{"booking":bk})

def mypublisherbook(request,id):
    cart = tbl_cart.objects.filter(booking=id)
    return render(request,"User/My_Publisher_Book.html",{"cart":cart})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    cart = tbl_cart.objects.get(id=mid)
    wdata=tbl_paddbook.objects.get(id=cart.product_id)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(book=cart.product_id).count()
    # print(cart.product_id)
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(book=wdata).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    cart=tbl_cart.objects.get(id=workid)
    wdata=tbl_paddbook.objects.get(id=cart.product_id)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,book=wdata)
    stardata=tbl_rating.objects.filter(book=wdata).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def userrating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    cart = tbl_swap.objects.get(id=mid)
    wdata=tbl_user.objects.get(id=cart.fromuser_id_id)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(user=cart.fromuser_id_id).count()
    # print(cart.product_id)
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(user=wdata).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/UserRating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/UserRating.html",{'mid':mid})
    
def userajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    cart=tbl_swap.objects.get(id=workid)
    wdata=tbl_user.objects.get(id=cart.fromuser_id_id)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,user=wdata)
    stardata=tbl_rating.objects.filter(user=wdata).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def viewuser(request,id):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0 
    ubook = tbl_uaddbook.objects.get(id=id)
    user = tbl_user.objects.get(id=ubook.user_id)
    tot=0
    ratecount=tbl_rating.objects.filter(user=user).count()
    if ratecount>0:
        ratedata=tbl_rating.objects.filter(user=user)
        for j in ratedata:
            tot=tot+j.rating_data
            avg=tot//ratecount
            #print(avg)
        parry.append(avg)
    else:
        parry.append(0)
    # print(parry)
    return render(request,"User/ViewUser.html",{"user":user,"parry":parry,"ar":ar})




def MyGenre(request):
    myGenre=tbl_usergenre.objects.all()
    Genredata=tbl_genre.objects.all()
    if request.method =='POST':
        user = tbl_user.objects.get(id=request.session['uid'])
        ugen=tbl_genre.objects.get(id=request.POST.get('selgenre'))
        tbl_usergenre.objects.create(
            genre=ugen,
            user=user,
        )
        return redirect('User:MyGenre')
    else:
        return render(request,"User/MyGenre.html",{'myGenre':myGenre,'Genredata':Genredata}) 


def MyWishList(request,id):
    user = tbl_user.objects.get(id=request.session['uid'])
    checkBook=tbl_wishlist.objects.filter(user=user,book=id)
    msg = ''
    if checkBook:
        return render(request,"User/searchp.html",{"msg":"Already Added"})
    else:
         ubook=tbl_paddbook.objects.get(id=id)
         tbl_wishlist.objects.create(
            book=ubook,
            user=user,
        )
         return render(request,"User/searchp.html",{"msg":"Added to WishList"})
   

def GenreDel(request,id):
    tbl_usergenre.objects.get(id=id).delete()
    return redirect('User:MyGenre')

def ViewWishList(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    data = tbl_wishlist.objects.filter(user=user)
    return render(request,"User/ViewWishList.html",{"data":data})
