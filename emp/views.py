from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
import simplejson
from .models import User

# Create your views here.
"""
 # 增
    #
    # models.Tb1.objects.create(c1='xx', c2='oo')  增加一条数据，可以接受字典类型数据 **kwargs

    # obj = models.Tb1(c1='xx', c2='oo')
    # obj.save()

    # 查
    #
    # models.Tb1.objects.get(id=123)         # 获取单条数据，不存在则报错（不建议）
    # models.Tb1.objects.all()               # 获取全部
    # models.Tb1.objects.filter(name='seven') # 获取指定条件的数据

    # 删
    #
    # models.Tb1.objects.filter(name='seven').delete() # 删除指定条件的数据

    # 改
    # models.Tb1.objects.filter(name='seven').update(gender='0')  # 将指定条件的数据更新，均支持 **kwargs
    # obj = models.Tb1.objects.get(id=1)
    # obj.c1 = '111'
    # obj.save()                                                 # 修改单条数据

"""


def login(request:HttpRequest):
    ret_dict = {
        "code": 0
        , "count": 0
        , "data": {}
    }
    user_info = simplejson.loads(request.body)
    if request.method == "GET":
        # todo 查询是用户是否存在
        username = user_info.get('name')
        user = User.objects.get(name=username)
        if len(user) > 0:
            ret_dict["code"] = 201
            ret_dict["count"] = len(user)
            ret_dict["data"] = "用户存在！"
        else:
            ret_dict["code"] = 205

    elif request.method == "POST":
        # todo 新增用户
        User.objects.create(**user_info)
        ret_dict["code"] = 206
        ret_dict["data"] = "add ok！"

    return HttpResponse(simplejson.dumps(ret_dict))


def list_emp(request:HttpRequest):
    # get all users and teturn to front
    ret_dict = {
        "code": 0
        , "count": 0
        , "data": {}
    }
    if request.method == "GET":
        user_qset=User.objects.all()
        if len(user_qset)>0:
            ret_dict["code"] = '200'
            ret_dict["count"] = len(user_qset)
            ret_dict["date"]=[]
            for user in user_qset:
                ret_dict['date'].append(user.name)

        else:
            ret_dict["code"] = '300'
            ret_dict["data"] = "no user"

    return HttpResponse(simplejson.dumps(ret_dict))

