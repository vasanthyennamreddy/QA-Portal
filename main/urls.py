from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = "home"),
    path('login/',views.loginpage, name = "loginpage"),
    path('logout/',views.logoutUser,name = "logout"),
    path('register/',views.register, name = "register"),
    path('teachers/',views.teachers,name="teachers"),
    path('createquestion/<str:istrid>',views.createquestion,name="createquestion"),
    path('istrnotifs/',views.istrnotifs,name="istrnotifs"),
    path('studnotifs/',views.studnotifs,name="studnotifs"),
    path('myans/',views.myans,name="myans"),
    path('update_ques/<str:pk>',views.update_ques,name="update_ques"),
    path('pending/',views.pending,name="pending"),
]

