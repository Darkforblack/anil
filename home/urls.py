
from django.urls import path
from . import views

#kumar ---.teacher
# password == >   4Ukumar@gmail.com  

#admin 
# password == >   admin

#anilkumar --> student 
# password == >   anilkumar@gmail.com4U

 
urlpatterns = [
    path('', views.index, name="index"),  
    path('login', views.handellogin, name="login"),
    path('handellogout', views.handellogout, name="handellogout"),
    path('register/', views.register, name="register"),
    path('mainindex', views.mainindex, name="mainindex"),
    path('mainindex2', views.mainindex2, name="mainindex2"),
     path('profile', views.profile, name="profile"),
    path('pro_student', views.pro_student, name="pro_student"),
     path('dash', views.dash, name="dash"),
     path('addcourse', views.addcourse, name="addcourse"),
     path('allcourse', views.allcourse, name="allcourse"),
     ]