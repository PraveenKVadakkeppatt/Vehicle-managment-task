"""VehicleManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PeojectApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('base', views.base, name='base'),

    path('load_signup', views.load_signup, name='load_signup'),
    # path('user_signup', views.user_signup, name='user_signup'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('user_login', views.user_login, name='user_login'),
    path('add_registration', views.add_registration, name='add_registration'),
    path('admin_welcome', views.admin_welcome, name='admin_welcome'),
    path('admin_showtable', views.admin_showtable, name='admin_showtable'),
    path('super_admin', views.super_admin, name='super_admin'),
    path('vehicle_registration', views.vehicle_registration, name='vehicle_registration'),
    path('add_vehicle', views.add_vehicle, name='add_vehicle'),
    path('super_admin_RegisteredVehicles', views.super_admin_RegisteredVehicles, name='super_admin_RegisteredVehicles'),
    path('editpage/<int:pk>', views.editpage, name='editpage'),
    path('edit_details/<int:pk>',views.edit_details,name='edit_details'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('editpage1/<int:pk>', views.editpage1, name='editpage1'),
    path('super_admin_welcome', views.super_admin_welcome, name='super_admin_welcome'),
    path('designation', views.designation, name='designation'),
    path('add_designation', views.add_designation, name='add_designation'),
    path('user_show_table', views.user_show_table, name='user_show_table'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('edit4admin/<int:pk>', views.edit4admin, name='edit4admin'),
    path('edit_details2/<int:pk>',views.edit_details2,name='edit_details2'),
]
