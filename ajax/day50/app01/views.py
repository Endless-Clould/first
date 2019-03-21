from django.shortcuts import render, HttpResponse
import json, os
from django.http import JsonResponse


# Create your views here.
# 初体验
def text(request):
    if request.method == "GET":
        return render(request, "text.html")
    else:
        return HttpResponse("OKOK")

# 计算
def total(request):
    ret = {'status': True, 'msg': None}
    try:
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        total = int(num1) + int(num2)
        ret["total"] = total
    except Exception as e:
        ret["status"] = False
        ret['msg'] = "输入有误"
    return HttpResponse(json.dumps(ret))


# 获取上传数据
def json_upload(request):
    print(request.POST)
    print(request.body)
    data = json.loads(request.body.decode("utf-8"))
    print(data, type(data))
    return HttpResponse("KOKO")
from django.core.files.uploadedfile import InMemoryUploadedFile
# 获取上传文件
def upload_file(request):
    print(request.POST)
    print(request.FILES)
    file_obj =request.FILES.get("file_name")
    print(file_obj.name,type("file_obj"))
    with open(os.path.join("medio",file_obj.name),"wb") as f :
        for line in file_obj:
            f.write(line)
    return HttpResponse("kalklakl")

def user(request):
    print(request.POST)
    print(request.body)
    data = json.loads(request.body.decode("utf-8"))
    print(data)
    return HttpResponse("kkkkkk")