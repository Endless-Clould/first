from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from  app01 import models
# Create your views here.
info ={"status":False}
def wapper(f):
    def inner(*args,**kwargs):
        if info["status"]:
            ret =f(*args,**kwargs)
            return ret
        else:
            return redirect("/val_login/")
    return inner
def login(request):
    ret =''
    if request.method =="POST":
        user =request.POST.get("user")
        pwd =request.POST.get("pwd")
        user_obj =models.UserInfo.objects.filter(username=user,password=pwd).first()
        if user_obj:
            obj=redirect('/index/')
            obj.set_cookie("is_login",True)
            obj.set_cookie("username",user_obj.username)
            return obj
        else:
            ret ="用户或者密码错误"
    return render(request,"login.html",{
        "ret":ret
    })

def index(request):
    is_login =request.COOKIES.get("is_login")
    username=request.COOKIES.get("username")
    if not is_login:
        return redirect("/login/")
    return render(request,"index.html",{
        "user":username
    })

import random



def val_login(request):
    ret ="123"
    if request.method == "POST":
        valid_code = request.POST.get("valid_code")
        username = request.POST.get("username")
        pwd = request.POST.get('pwd')
        keep_str = request.session.get('keep_str')
        print(valid_code)
        print(username)
        print(pwd)
        print(keep_str)
        if valid_code.upper() == keep_str.upper():
            user_obj = models.UserInfo.objects.filter(username=username, password=pwd).first()
            if user_obj:
                request.session["is_login"] = True
                request.session["username"] = user_obj.username
                info["status"]=True
                # obj = redirect("/s_index/")
                return redirect("/val_index/")
            else:
                ret ="用户或者密码错误"

        else:
            ret="验证码错误"
    return render(request, "login1.html",{
        "ret":ret
    })

def val_index(request):
    is_login=request.session.get("is_login")
    username=request.session.get("username")
    if not is_login:
        return redirect("/val_login/")
    return render(request,"index.html",
                  {
                      "user":username
                  })

def get_random_color():
    """
    获取随机图片颜色
    :return:
    """
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def val_img(request):
    from io import BytesIO
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (250, 40), get_random_color())  # 新建图片大小为250*40
    draw = ImageDraw.Draw(img)  # 可以在该图片对象上写内容
    font = ImageFont.truetype("statics/qita/font.ttf", 30)  # 指定字体，需自行下载字体文件

    keep_str = ""
    for i in range(5):  # 获取随机数
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(97, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((20 + i * 35, 0), random_char, get_random_color(), font=font)
        keep_str += random_char

    # 噪点噪线
    # width=250
    # height=40
    # for i in range(10):
    #     x1=random.randint(0,width)
    #     x2=random.randint(0,width)
    #     y1=random.randint(0,height)
    #     y2=random.randint(0,height)
    #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    #
    # for i in range(100):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    request.session["keep_str"] = keep_str
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()

    return HttpResponse(data)

@wapper
def val_list(request):
    return HttpResponse("这是图书馆里界面")

