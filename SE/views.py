from django.shortcuts import render,HttpResponse,redirect
from SE import models
import datetime
import re
import json
# Create your views here.
def dianya(requset):
    if requset.method == "POST":
        dianya_list = models.value.objects.filter(user_id=new_account_id_list[new_account_id_list.__len__()-1]).values("dianya")
        dianya_len = dianya_list.__len__()
        # 获取监控值
        dianya_value = float(dianya_list[dianya_len - 1]['dianya'])

        time_list = models.value.objects.values("time")
        time_len = time_list.__len__()
        # 获取时间
        time_value = time_list[time_len - 1]['time']
        dianya_y,dianya_mon,dianya_d,dianya_h,dianya_m,dianya_s = re_time(time_value)
        #传到js的数据
        dianya_list = [
            {"dianya_value": dianya_value},
            {'dianya_y': dianya_y},
            {'dianya_mon': dianya_mon},
            {'dianya_d': dianya_d},
            {'dianya_h': dianya_h},
            {'dianya_m': dianya_m},
            {'dianya_s': dianya_s},
        ]

        return HttpResponse(json.dumps(dianya_list))
    return render(requset, 'dianya.html')

def dianliang(requset):
    if requset.method == "POST":
        dianliang_list = models.value.objects.filter(user_id=new_account_id_list[new_account_id_list.__len__()-1]).values("dianliang")
        dianliang_len = dianliang_list.__len__()
        # 获取监控值
        dianliang_value = float(dianliang_list[dianliang_len - 1]['dianliang'])

        time_list = models.value.objects.values("time")
        time_len = time_list.__len__()
        # 获取时间
        time_value = time_list[time_len - 1]['time']

        dianliang_y,dianliang_mon,dianliang_d,dianliang_h,dianliang_m,dianliang_s = re_time(time_value)
        #传到js的数据
        dianliang_list = [
            {"dianliang_value": dianliang_value},
            {'dianliang_y': dianliang_y},
            {'dianliang_mon': dianliang_mon},
            {'dianliang_d': dianliang_d},
            {'dianliang_h': dianliang_h},
            {'dianliang_m': dianliang_m},
            {'dianliang_s': dianliang_s},
        ]

        return HttpResponse(json.dumps(dianliang_list))
    return render(requset, 'dianliang.html')

def gonglv(requset):
    if requset.method == "POST":
        gonglv_list = models.value.objects.filter(user_id=new_account_id_list[new_account_id_list.__len__()-1]).values("gonglv")
        gonglv_len = gonglv_list.__len__()
        # 获取监控值
        gonglv_value = float(gonglv_list[gonglv_len - 1]['gonglv'])

        time_list = models.value.objects.values("time")
        time_len = time_list.__len__()
        # 获取时间
        time_value = time_list[time_len - 1]['time']

        gonglv_y, gonglv_mon, gonglv_d, gonglv_h, gonglv_m, gonglv_s = re_time(time_value)
        #传到js的数据
        gonglv_list = [
            {"gonglv_value": gonglv_value},
            {'gonglv_y': gonglv_y},
            {'gonglv_mon': gonglv_mon},
            {'gonglv_d': gonglv_d},
            {'gonglv_h': gonglv_h},
            {'gonglv_m': gonglv_m},
            {'gonglv_s': gonglv_s},
        ]

        return HttpResponse(json.dumps(gonglv_list))
    return render(requset, 'gonglv.html')


def dianliu(requset):
    if requset.method == "POST":
        dianliu_list = models.value.objects.filter(user_id=new_account_id_list[new_account_id_list.__len__()-1]).values("dianliu")
        dianliu_len = dianliu_list.__len__()
        #获取监控值
        dianliu_value = float(dianliu_list[dianliu_len-1]['dianliu'])

        time_list = models.value.objects.values("time")
        time_len = time_list.__len__()
        # 获取时间
        time_value = time_list[time_len - 1]['time']

        dianliu_y,dianliu_mon,dianliu_d,dianliu_h,dianliu_m,dianliu_s = re_time(time_value)
        #传到js的数据
        dianliu_list = [
            {"dianliu_value": dianliu_value},
            {'dianliu_y': dianliu_y},
            {'dianliu_mon': dianliu_mon},
            {'dianliu_d': dianliu_d},
            {'dianliu_h': dianliu_h},
            {'dianliu_m': dianliu_m},
            {'dianliu_s': dianliu_s},
        ]

        return HttpResponse(json.dumps(dianliu_list))
    return render(requset, 'dianliu.html')

E_Value = {}
def re_data(data):
    E_A = re.match(r'(.*)A(.*)V(.*)W(.*)C',data, re.I).group(1)
    E_V = re.match(r'(.*)A(.*)V(.*)W(.*)C',data, re.I).group(2)
    E_W = re.match(r'(.*)A(.*)V(.*)W(.*)C',data, re.I).group(3)
    E_C = re.match(r'(.*)A(.*)V(.*)W(.*)C',data, re.I).group(4)
    E_Value['E_A'] = E_A
    E_Value['E_V'] = E_V
    E_Value['E_W'] = E_W
    E_Value['E_C'] = E_C
    print(E_Value)
    return E_Value

def re_time(time):
    pattern = re.compile(r'(.*)-(.*)-(.*) (.*):(.*):(.*)\.')
    year = pattern.search(time).group(1)
    month = remove_0(pattern.search(time).group(2))
    day = remove_0(pattern.search(time).group(3))
    hour = remove_0(pattern.search(time).group(4))
    min = remove_0(pattern.search(time).group(5))
    sec = remove_0(pattern.search(time).group(6))
    return year,month,day,hour,min,sec

def remove_0(date):
    if date[0] == "0":
        date = date[1:len(date)]
    return date


def recv_data(request):
    if request.method == "POST":
        #获取数据
        recv_data = request.POST['recv_data']
        print(recv_data)

        Value_dic= re_data(recv_data)    #正则匹配数据
        times = datetime.datetime.now()  #获取现在时间
        #把数据存储在数据库中
        models.value.objects.filter(user_id=new_account_id_list[new_account_id_list.__len__()-1]).create(
            dianliu = Value_dic['E_A'],
            dianya = Value_dic['E_V'],
            dianliang = Value_dic['E_C'],
            gonglv = Value_dic['E_W'],
            time=times,
            user_id=new_account_id_list[new_account_id_list.__len__()-1]
        )
        return HttpResponse('ok')
    else:
        return redirect('/login/')

def login(request):
    if request.method =='POST':
        #获取用户的用户名和密码
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        username1 =username
        #获取用户信息列表
        user_list = models.user_info.objects.filter()
        print(user_list)
        #循环Queryset，做用户验证
        for user in user_list:
            if username == user.username:
                if  password == user.password:
                    #获取id
                    new_account = models.user_info.objects.filter(username=username)
                    new_account_id_list.append(new_account[0].id)
                    return HttpResponse(json.dumps(1))
                else:
                    return HttpResponse(json.dumps(2))
            else:
                return HttpResponse(json.dumps(3))
    return render(request,'login.html')

new_account_id_list = []
def create_account(request):
    if request.method =='POST':
        #获取用户的用户名和密码
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # 获取用户信息列表
        user_list = models.user_info.objects.filter()
        for user in user_list:
            if username != user.username:
                if  email != user.e_mail:
                    # 把信息写入数据库
                    models.user_info.objects.create(username=username, password=password, e_mail=email)
                    # 获取id
                    new_account = models.user_info.objects.filter(username=username)
                    new_account_id_list.append(new_account[0].id)
                    return HttpResponse(json.dumps(1))
                else:
                    return HttpResponse(json.dumps(2))
            else:
                return HttpResponse(json.dumps(3))
        if user_list.__len__() == 0:
            # 把信息写入数据库
            models.user_info.objects.create(username=username, password=password, e_mail=email)
            # 获取id
            new_account = models.user_info.objects.filter(username=username)
            new_account_id_list.append(new_account[0].id)
            return HttpResponse(json.dumps(1))
    return render(request,'create_account.html')



































