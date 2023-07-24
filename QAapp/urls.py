from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('detail/<int:pk>/',views.detail,name='home'),
    path('ask/',views.ask,name='ask'),
    
    path('accounts/register/',views.register,name='register'),
    path('accounts/login/',views.loginpage,name='login'),
    path('accounts/logout',views.signout,name='logout'),
]