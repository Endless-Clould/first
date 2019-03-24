from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from app01 import models


# Create your views here.
def show_list(request):
    is_login =request.session.get("is_login")
    username =request.session.get("username")
    if not is_login:
        return redirect("/login/")
    book = models.Book.objects.all()
    # print(book)
    return render(request, "book_list.html",
                  {
                      "books": book
                  })


def add_book(request):
    if request.method == "GET":
        publishs = models.Publish.objects.all()
        authors = models.Author.objects.all()
        return render(request, "add_book.html",
                      {
                          "publishs": publishs,
                          "authors": authors

                      })
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        author_list = request.POST.getlist("author")
        publish = request.POST.get("publish")
        print(title, price, pub_date, author_list, publish)
        book = models.Book.objects.create(title=title, price=price, pub_date=pub_date,
                                          publish_id=publish)
        book.authors.add(*author_list)
        return redirect(reverse("showlist"))


def ajax_add_book(request):
    if request.method == "GET":
        publishs = models.Publish.objects.all()
        authors = models.Author.objects.all()
        return render(request, "add_book.html",
                      {
                          "publishs": publishs,
                          "authors": authors

                      })
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        author_list = request.POST.getlist("author")
        publish = request.POST.get("publish")
        print(title, price, pub_date, author_list, publish)
        book = models.Book.objects.create(title=title, price=price, pub_date=pub_date,
                                          publish_id=publish)
        book.authors.add(*author_list)
        return redirect(reverse("showlist"))






def update_book(request, book_id):
    if request.method == "GET":
        book_obj = models.Book.objects.filter(pk=book_id).first()
        # print(title.first().title)
        authors = models.Author.objects.all()
        publishs = models.Publish.objects.all()
        print(publishs, type(publishs))
        return render(request, "update.html", {
            "book_obj": book_obj,
            "authors": authors,
            "publishs": publishs

        })
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        author_list = request.POST.getlist("author")
        publish = request.POST.get("publish")
        print(title, price, pub_date, author_list, publish)
        book = models.Book.objects.filter(pk=book_id).update(title=title, price=price, pub_date=pub_date,
                                                             publish_id=publish)
        bok = models.Book.objects.filter(pk=book_id).first()
        bok.authors.set(author_list)
        return redirect(reverse("showlist"))


def del_book(request, book_id):
    book = models.Book.objects.filter(pk=book_id).delete()
    return redirect(reverse("showlist"))


def del_book1(request):
    # print(book_id)
    ret = {"static": True, "msg": None}
    book_title = request.POST.get("book_id")
    print(book_title)
    # print(book_title)
    ret["msg"] = book_title
    book = models.Book.objects.filter(pk=book_title).delete()
    return JsonResponse(ret)
    # return HttpResponse(book_title)


from django.http import JsonResponse
import json


def login(request):
    ret = {"static": False, "msg": "账号或者密码错误"}
    if request.method == "POST":
        valid_code = request.POST.get("valid_code")
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        keep_str = request.session.get('keep_str')
        print(valid_code)
        print(user)
        print(pwd)
        print(keep_str)
        if valid_code.upper() == keep_str.upper():
            user_obj = models.User.objects.filter(username=user, password=pwd).first()
            if user_obj:
                request.session["is_login"] = True
                request.session["username"] = user_obj.username
                ret["static"] = True
                ret =json.dumps(ret)
                print(ret,type("ret"))
                return HttpResponse(ret)
            else:
                ret["msg"] = "账号或者密码错误"
                ret = json.dumps(ret)
                return HttpResponse(ret)
        else:

            ret["msg"] = "验证码错误"
            ret = json.dumps(ret)
            return HttpResponse(ret)
    return render(request, "login.html", {
    })


import random


def get_random_color():
    """
    获取随机图片颜色
    :return:
    """
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def val_img(request):
    from io import BytesIO
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (550, 140), get_random_color())  # 新建图片大小为250*40
    draw = ImageDraw.Draw(img)  # 可以在该图片对象上写内容
    font = ImageFont.truetype("statics/other/font.ttf", 30)  # 指定字体，需自行下载字体文件

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


def show(request):
    return render(request, "show.html")


'''             
聚合查询
'''
from django.db.models import Avg, Max, Min, Count, Sum
from django.db.models import F, Q


def test(request):
    # books =models.Book.objects.aggregate(Avg("price")) 打印平均值
    # books =models.Book.objects.aggregate(Max("price"),Min("price"),Count("price"),Sum("price"))
    # emp =models.Emp.objects.values("dep").annotate(Count("id"))
    # print(books)
    # emp =models.Emps.objects.values("dep__title").annotate(Count("dep_id"))
    # emp =models.Emp.objects.values("dep").annotate(Avg("salary"))
    # emp =models.Emps.objects.values("dep__title").annotate(Avg("salary"))
    # print(emp)
    # pub =models.Publish.objects.values("name").annotate(Min("book__price"))
    # pub =models.Publish.objects.values("name").aggregate(Min("book__price"))

    # book =models.Book.objects.values("title").annotate(Count("authors__id"))
    # book =models.Book.objects.filter(title__startswith="独").values("title").annotate(Count("authors__id"))
    # book = models.Book.objects.filter(title__startswith="独").values("title").annotate(Count('authors__id'))
    # book =models.Book.objects.values("title").annotate(num =Count("authors__id")).filter(num__gt=1)
    # print(book)

    # book =models.Emp.objects.filter(salary__gt=F("age"))
    # book =models.Emp.objects.filter(salary__lt=F("age")*2)
    book = models.Book.objects.update(price=F("price") + 100)
    print(book)
    return HttpResponse("ff654d2k")
