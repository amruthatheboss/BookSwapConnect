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

]
