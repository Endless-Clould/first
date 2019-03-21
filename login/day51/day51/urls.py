"""day51 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app01 import views
from app02 import views as s_views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("login/",views.login,name="login"),
    path("index/",views.index,name="index"),
    path("s_login/",s_views.s_login,name="s_login"),
    path("s_index/",s_views.s_index,name="s_index"),
    path("s_out/",s_views.s_out),
    path("val_login/",views.val_login),
    path("val_img/",views.val_img,name="valimg"),
    path("val_index/",views.val_index),
    path("val_list/",views.val_list)
]
