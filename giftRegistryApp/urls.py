"""giftAway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    
    url(r'^index/$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='login'),
    url(r'^changepassword', views.change_password, name='changepassword'),
    url(r'^newuser', views.register_new_user, name='register_new_user'),
    url(r'^createregistry', views.create_registry_api, name='create_registry_api'),
    url(r'^registries', views.get_registries, name='get_registry_api'),
    url(r'^userdetails', views.get_user_details, name='get_user_details'),
    url(r'^assignitem', views.assign_item, name='get_user_details'),
    url(r'^unassignitem', views.unassign_item, name='get_user_details'),
    url(r'^getregistry', views.get_registry_details, name='get_registry_details'),
    url(r'^additemtoregistry', views.add_item_to_registry, name='get_registry_details'),
    url(r'^items', views.get_items, name='get_items'),
    url(r'^getusers', views.get_users, name='get_users'),
    url(r'^forgotpassword', views.forgot_password, name='forgot_password'),
    url(r'^additemtoinventory', views.add_item_to_inventory, name='add_item_to_inventory'),
    url(r'^removeitemfrominventory', views.remove_item_from_inventory, name='remove_item_from_inventory'),
    url(r'^removeitemfromregistry', views.remove_item_from_registry, name='remove_item_from_registry'), 
]
