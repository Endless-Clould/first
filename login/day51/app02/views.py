from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from app01 import models
def s_login(request):
    ret =''
    if request.method =="POST":
        user= request.POST.get("user")
        pwd =request.POST.get("pwd")
        user_obj =models.UserInfo.objects.filter(username=user,password=pwd).first()
        if user_obj:
            request.session["is_login"]=True
            request.session["username"]=user_obj.username
            obj =redirect("/s_index/")
            return obj
        else:
            ret ="用户名或者密码错误"
    return render(request,"login.html",{
        "ret":ret
    })

def s_index(request):
    is_login =request.session.get("is_login")   # 拿到 前端的session id  乱码
    username =request.session.get("username")      # 拿到前端的 username  乱码
    if not is_login:
        return redirect("/s_login/")
    return render(request,"index.html",{
        "user":username
    })
def s_out(request):
    request.session.flush()
    return redirect("/val_login/")