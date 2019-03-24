"""dy49 URL Configuration

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
from django.urls import path,re_path
from app01 import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('showlist/',views.show_list,name="showlist"),
    path('addbook/',views.add_book,name="addbook"),
    re_path(r'^update/(?P<book_id>\d+)/$',views.update_book,name="updatebook"),
    re_path(r'^del//(?P<book_id>\d+)/',views.del_book,name="delbook"),
    path('del/',views.del_book1,name="delbook1"),
    path('text/',views.test),
    path("login/",views.login,name="login"),
    path("val_img/",views.val_img,name="valimg"),
    path("show/",views.show),
    path("add_book2/",views.ajax_add_book,name="ajax_add_book")
]
