"""
URL configuration for project9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,re_path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',Home.as_view(),name='Home'),
    path('School_list/',School_list.as_view(),name='School_list'),
    path('School_form/',School_form.as_view(),name='School_form'),
    path('Student_form/',Student_form.as_view(),name='Student_form'),

    re_path('^update(?P<pk>\d+)/',School_Update.as_view(),name='School_Update'),
    re_path('^Delete(?P<pk>\d+)/',School_Delete.as_view(),name='School_Delete'),
    re_path('(?P<pk>\d+)/',School_Detail.as_view(),name='School_Detail'),
]
