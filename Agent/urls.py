from django.urls import path
from Agent import views
app_name="Agent"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('vieworders/',views.vieworders,name="vieworders"),

    path('take_order/<int:id>',views.take_order,name="take_order"),
    path('order_collected/<int:id>',views.order_collected,name="order_collected"),
    path('order_delivered/<int:id>',views.order_delivered,name="order_delivered"),
    path('order_returned/<int:id>',views.order_returned,name="order_returned"),
    path('returned_delivered/<int:id>',views.returned_delivered,name="returned_delivered"),

    path('viewproduct/<int:id>',views.viewproduct,name="viewproduct"),
    path('viewpublisherproduct/<int:id>',views.viewpublisherproduct,name="viewpublisherproduct"),
    path('myorders/',views.myorders,name="myorders"),

    path('getutouorder/<int:id>',views.getutouorder,name="getutouorder"),
    path('getptouorder/<int:id>',views.getptouorder,name="getptouorder"),

    path('collect_utou_order/<int:id>',views.collect_utou_order,name="collect_utou_order"),
    path('delivered_utou_order/<int:id>',views.delivered_utou_order,name="delivered_utou_order"),

    path('collect_ptou_order/<int:id>',views.collect_ptou_order,name="collect_ptou_order"),
    path('delivered_ptou_order/<int:id>',views.delivered_ptou_order,name="delivered_ptou_order"),


    path('logout/',views.logout,name="logout"),

]
