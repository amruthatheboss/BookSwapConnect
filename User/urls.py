from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('UserAddBook/',views.UserAddBook,name="UserAddBook"),
    path('UserBookDel/<int:id>',views.UserBookDelete,name="UserBookDel"),
    path('UserBookUpdate/<int:eid>',views.UserBookupdate,name="UserBookUpdate"),

    path('Search/',views.searchbook,name="Search"),

    path('Ajaxsearch/',views.ajaxsearch,name="Ajaxsearch"),

    path('Viewmore/<int:bid>',views.Viewmore,name="Viewmore"),


    path('Swaprequest/<int:bid>',views.Swaprequest,name="Swaprequest"), 
    path('Viewrequest/',views.Viewrequest,name="Viewrequest"),
    path('Viewbooks/<int:Fromid>/<int:sid>',views.Viewbooks,name="Viewbooks"),

    path('Acceptbook/<int:bid>/<int:sid>',views.Acceptbook,name="Acceptbook"),

    path('payment/<int:amt>/<int:sid>',views.payment,name="payment"),

    path('mybooking/',views.mybooking,name="mybooking"),
    path('view_publisher_book/',views.view_publisher_book,name="view_publisher_book"),

     path('usercomplaint/',views.usercomplaint,name="usercomplaint"),

     path('Viewcomplaints/',views.Viewcomplaints,name="Viewcomplaints")

]
