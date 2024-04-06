from django.urls import path
from Admin import views
 

app_name = "webadmin"

urlpatterns = [


    path('HomePage/', views.LoadAdminHome,name="LoadAdminHome"),
    
    path('District/', views.districtInsertSelect, name='districtInsertSelect'),
    path('DistrictDel/<int:id>', views.Districtdelete, name='DistrictDel'),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),

    path('Category/', views.Category, name='Category'),
    path('CategoryDel/<int:id>', views.Categorydelete, name='CatDel'),
    path('Categoryupdate/<int:eid>',views.Categoryupdate, name="Categoryupdate"),

    

    path('Registration/',views.Registration, name='Registration'),
    path('RegistrationDel/<int:id>', views.Registrationdelete, name='RegistrationDel'),
    path('Registrationupdate/<int:eid>',views.Registrationupdate, name="Registrationupdate"),

    path('Publisher/',views.Publisher, name='Publisher'),
    path('PublisherDel/<int:id>', views.Publisherdelete, name='PublisherDel'),
    path('Publisherupdate/<int:eid>',views.Publisherupdate,name="Publisherupdate"),
    
    path('place/', views.Place, name='Place'),

    path('Subcategory/', views.Subcategory, name='Subcategory'),
    
    path('PlaceDel/<int:id>', views.Placedelete, name='PlaceDel'),

    path('SubcategoryDel/<int:id>', views.Subcategorydelete, name='SubcategoryDel'),
    
    path('Genre/', views.Genre, name='Genre'),
    path('Genredel/<int:id>', views.Genredelete, name='Genredel'),
    path('Genreupdate/<int:eid>',views.Genreupdate,name="Genreupdate"),


    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),

    path('PublisherListNew/',views.publisherListNew,name="publisherListNew"),
    path('acceptpub/<int:aid>',views.acceptpub,name="acceptpub"),
    path('rejectpub/<int:rid>',views.rejectpub,name="rejectpub"),
    path('PublisherListAccepted/',views.publisherListAccepted,name="publisherListAccepted"),
    path('PublisherListRejected/',views.publisherListRejected,name="publisherListRejected"),

    path('AgentListNew/',views.agentListNew,name="agentListNew"),
    path('acceptagent/<int:aid>',views.acceptagent,name="acceptagent"),
    path('rejectagent/<int:rid>',views.rejectagent,name="rejectagent"),
    path('AgentListAccepted/',views.agentListAccepted,name="agentListAccepted"),
    path('AgentListRejected/',views.agentListRejected,name="agentListRejected"),

    path('Quality/', views.Quality, name='Quality'),
    path('Qualitydel/<int:id>', views.Qualitydelete, name='Qualitydel'),
    path('Qualityupdate/<int:eid>',views.Qualityupdate,name="Qualityupdate"),

    path('vieworders/', views.vieworders, name='vieworders'),
    path('completed/<int:id>',views.completed,name="completed"),

    path('Reply/<int:id>', views.reply, name='reply'),
    path('Viewcomplaint/', views.viewcomplaint, name='viewcomplaint'),


]