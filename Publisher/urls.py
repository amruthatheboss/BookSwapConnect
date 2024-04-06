from django.urls import path
from Publisher import views
app_name="Publisher"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('PublisherAddBook/',views.PublisherAddBook,name="PublisherAddBook"),
    path('PublisherBookDel/<int:id>',views.PublisherBookdelete,name="PublisherBookDel"),
    path('PublisherBookUpdate/<int:eid>',views.PublisherBookupdate,name="PublisherBookUpdate"),

    path('publishercomplaint/',views.publishercomplaint,name="publishercomplaint"),
    path('Viewpublishercomplaints/',views.Viewpublishercomplaints,name="Viewpublishercomplaints"),
    path('logout/',views.logout,name="logout"),
]
