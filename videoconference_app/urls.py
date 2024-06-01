from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('JoinMeeting',views.JoinMeeting,name='joinMeeting'),
    path('NewMeeting',views.videoCall,name='newMeeting'),
    path('logout/',views.Logout_user,name='logout'),
    path('',views.index, name='index'),


]