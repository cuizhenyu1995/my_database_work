# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from .models import user, device, buy_device, lend_device, repair_device
import json
from django.core import serializers
from json_response import JsonResponse
import traceback
from datetime import datetime
# import time


# 注册
def regist(request):
    if request.method == 'POST':
        # uf = UserFormRegist(req.POST)
        if request.POST.get('Submit', 'xxx') == u"注册":
            # 获得表单数据
            username = request.POST.get('username')
            password = request.POST.get('password')
            st_name = request.POST.get('st_name')
            st_sex = request.POST.get('st_sex', 'xxx')
            st_age = request.POST.get('st_age')
            st_address = request.POST.get('st_address')
            # 添加到数据库
            user.objects.create(
                st_username = username,
                st_name = st_name,
                st_sex = st_sex,
                st_age = st_age,
                st_password = password,
                st_address = st_address,
            )
            response = HttpResponseRedirect('/online/regist_success/')
            return response
        elif request.POST.get('Submit','xxx') == u"登录":
            response = HttpResponseRedirect('/online/login/')
            return response
    else:
        return render(request, 'regist.html')

# 注册成功
def regist_success(request):
    return render(request, 'regist_success.html')

# 登陆
def login(request):
    if request.method == 'POST':
        # uf = UserFormLogin(req.POST)
        # 获取表单用户密码
        if request.POST.get('Submit','xxx') == u"登录":
            username = request.POST.get('username')
            password = request.POST.get('password')
            # 获取的表单数据与数据库进行比较
            myuser = user.objects.filter(st_username__exact=username, st_password__exact=password)
            if myuser:  # 比较成功，跳转index
                response = HttpResponseRedirect('/online/index/')
                response.set_cookie('username', username, 3600)  # 将username写入浏览器cookie,失效时间为3600
                return response
            else:  # 比较失败，还在login
                response = HttpResponseRedirect('/online/login/')
                return response
        elif request.POST.get('Submit','xxx') == u"注册":
            response = HttpResponseRedirect('/online/regist/')
            return response
    else:
        return render(request, 'login.html')

# 登陆成功-主界面
def index(request):
    response = HttpResponseRedirect('/online/index/')
    username = request.COOKIES.get('username', '')
    me = user.objects.get(st_username=username)
    context = {}
    context['username']=me.st_name
    return render(request, 'index.html',context)

# 退出
def logout(request):
    # 清理cookie里保存username
    response = HttpResponseRedirect('/online/logout/')
    response.delete_cookie('username')
    return render(request,'logout.html')

# 关于我们
def about(request):
    response = HttpResponseRedirect('/online/index/about/')
    return render(request,'about.html')

# 用户管理
def yhgl(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        response = HttpResponseRedirect('/online/index/yhgl/')
        return render(request,'yhgl.html')

# 用户管理-获取用户
def get_user(request):
    ans = []
    que = user.objects.filter()
    for elem in que:
        tmp={
            "st_username":elem.st_username,
            "st_name": elem.st_name,
            "st_sex": elem.st_sex,
            "st_age": elem.st_age,
            "st_password": elem.st_password,
            "st_address": elem.st_address,
        }
        if (tmp["st_sex"]==1):
            tmp["st_sex"]=u"男"
        else:
            tmp["st_sex"]=u"女"
        ans.append(tmp)
    return HttpResponse(json.dumps(ans), content_type="application/json")

# 用户管理-删除用户
def delete_user(request):

    # de_name=request
    de_name = request.POST.get(u'del_name')
    ret=[]
    try:
        user.objects.filter(st_username=de_name).delete()
        tmp={
            "stat":"1",
        }
    except:
        tmp = {
            "stat": "0",
        }
    ret.append(tmp)
    return HttpResponse(json.dumps(ret), content_type="application/json")

# 用户管理-编辑用户
def edit_user(request):
    ret = []
    print request.POST
    try:
        n_username = request.POST.get(u'st_username')
        n_name = request.POST.get(u'st_name')
        if request.POST.get(u'st_sex')==u'女':
            n_sex = '2'
        else:
            n_sex = '1'
        n_age = request.POST.get(u'st_age')
        # print "666"
        n_pass = request.POST.get(u'st_password')
        # print "777"
        n_address = request.POST.get(u'st_address')



        user.objects.filter(st_username=n_username).delete()
        user.objects.create(
            st_username=n_username,
            st_name=n_name,
            st_sex=n_sex,
            st_age=n_age,
            st_password=n_pass,
            st_address=n_address,
        )
        tmp = {
            "stat": "1",
        }
        ret.append(tmp)
    except Exception,mmm:
        # print mmm
        # print "888"
        tmp = {
            "stat": "0",
        }
        ret.append(tmp)
    return HttpResponse(json.dumps(ret), content_type="application/json")

# 用户管理-添加用户
def add_user(request):
    ret = []
    try:
        user.objects.create(
            st_username=request.POST.get(u'add_username'),
            st_name=request.POST.get(u'add_name'),
            st_sex=request.POST.get(u'add_sex'),
            st_age=request.POST.get(u'add_ygnl'),
            st_password=request.POST.get(u'add_mm'),
            st_address=request.POST.get(u'add_ygzz'),
        )
        tmp = {
            "stat": "1",
        }
        ret.append(tmp)
    except :
        tmp = {
            "stat": "0",
        }
        ret.append(tmp)
    return HttpResponse(json.dumps(ret), content_type="application/json")

# 个人资料
def grzl(request):
    response = HttpResponseRedirect('/online/index/grzl/')
    return render(request, 'grzl.html')

# 个人资料-获得自己
def get_me(request):
    ans = []
    que = user.objects.filter(st_username__exact = request.COOKIES.get('username', ''))
    print que
    for elem in que:
        tmp = {
            "st_username": elem.st_username,
            "st_name": elem.st_name,
            "st_sex": elem.st_sex,
            "st_age": elem.st_age,
            "st_password": elem.st_password,
            "st_address": elem.st_address,
        }
        if (tmp["st_sex"] == 1):
            tmp["st_sex"] = u"男"
        else:
            tmp["st_sex"] = u"女"
        ans.append(tmp)
    return HttpResponse(json.dumps(ans), content_type="application/json")

# 个人资料-编辑自己
def edit_me(request):
    ret = []
    print request.POST
    try:
        n_username = request.POST.get(u'st_username')
        n_name = request.POST.get(u'st_name')
        if request.POST.get(u'st_sex') == u'女':
            n_sex = '2'
        else:
            n_sex = '1'
        n_age = request.POST.get(u'st_age')
        # print "666"
        n_pass = request.POST.get(u'st_password')
        # print "777"
        n_address = request.POST.get(u'st_address')

        user.objects.filter(st_username=n_username).delete()
        user.objects.create(
            st_username=n_username,
            st_name=n_name,
            st_sex=n_sex,
            st_age=n_age,
            st_password=n_pass,
            st_address=n_address,
        )
        tmp = {
            "stat": "1",
        }
        ret.append(tmp)
    except Exception, mmm:
        # print mmm
        # print "888"
        tmp = {
            "stat": "0",
        }
        ret.append(tmp)
    return HttpResponse(json.dumps(ret), content_type="application/json")

# 添加设备
def tjsb(request):
    response = HttpResponseRedirect('/online/index/tjsb/')
    return render(request,'tjsb.html')

# 添加设备-获取设备
def get_device(request):
    ans = []
    que = device.objects.filter()
    for elem in que:
        tmp={
            "de_no":elem.de_no,
            "de_name": elem.de_name,
            "de_allnum": elem.de_allnum,
            "de_repnum": elem.de_repnum,
            "de_lennum": elem.de_lennum,
            "de_lasnum": elem.de_lasnum,
        }
        ans.append(tmp)
    return HttpResponse(json.dumps(ans), content_type="application/json")

# 添加设备-删除设备
def delete_device(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        # de_name=request
        de_no = request.POST.get(u'del_no')
        ret=[]
        try:
            device.objects.filter(de_no=de_no).delete()
            tmp={
                "stat":"1",
            }
        except:
            tmp = {
                "stat": "0",
            }
        ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")

# 添加设备-编辑设备
def edit_device(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html', context)
    else:
        ret = []
        # print request.POST
        try:
            n_de_no = request.POST.get(u'de_no')
            n_de_name = request.POST.get(u'de_name')

            device.objects.filter(de_no=n_de_no).delete()
            device.objects.create(
                de_no=n_de_no,
                de_name=n_de_name,
                de_allnum="0",
                de_repnum="0",
                de_lennum="0",
                de_lasnum="0",
            )
            tmp = {
                "stat": "1",
            }
            ret.append(tmp)
        except Exception,mmm:
            # print mmm
            # print "888"
            tmp = {
                "stat": "0",
            }
            ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")

# 添加设备-添加设备
def add_device(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        ret = []
        try:
            device.objects.create(
                de_no=request.POST.get(u'de_no'),
                de_name=request.POST.get(u'de_name'),
                de_allnum="0",
                de_repnum="0",
                de_lennum="0",
                de_lasnum="0",
            )
            tmp = {
                "stat": "1",
            }
            ret.append(tmp)
        except :
            tmp = {
                "stat": "0",
            }
            ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")

# 购买设备
def gmsb(request):
    response = HttpResponseRedirect('/online/index/gmsb/')
    return render(request,'gmsb.html')

# 购买设备-获取设备
def get_gmsb(request):
    ans = []
    que = buy_device.objects.filter()
    for elem in que:
        mbtime=elem.de_btime
        mptime=elem.de_ptime
        tmp={
            "buy_no": elem.buy_no,
            "de_no": elem.de_no,
            "de_btime": mbtime.strftime("%Y-%m-%d"),
            "de_ptime": mptime.strftime("%Y-%m-%d"),
            "buy_num": elem.buy_num,
            "beizhu": elem.beizhu,
        }
        # print tmp
        ans.append(tmp)
    return HttpResponse(json.dumps(ans), content_type="application/json")

# 购买设备-编辑设备
def edit_gmsb(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        ret = []
        # print request.POST
        try:
            n_buy_no = request.POST.get(u'buy_no')
            n_de_no = request.POST.get(u'de_no')
            n_de_btime = datetime.strptime(request.POST.get(u'de_btime'),"%Y-%m-%d")
            n_de_ptime = datetime.strptime(request.POST.get(u'de_ptime'),"%Y-%m-%d")
            n_buy_num = request.POST.get(u'buy_num')
            n_beizhu = request.POST.get(u'beizhu')
            # print type(n_buy_no)
            # print type(n_de_no)
            # print type(n_de_btime)
            # print type(n_de_ptime)
            # print type(n_buy_num)
            # print type(n_beizhu)

            buy_device.objects.filter(buy_no=n_buy_no).delete()
            # print "删除"
            buy_device.objects.create(
                buy_no=int(n_buy_no),
                de_no=n_de_no,
                de_btime=n_de_btime,
                de_ptime=n_de_ptime,
                buy_num=int(n_buy_num),
                beizhu=n_beizhu,
            )
            # print "添加"
            tmp = {
                "stat": "1",
            }
            ret.append(tmp)
        except Exception,mmm:
            # print mmm
            # print "888"
            tmp = {
                "stat": "0",
            }
            ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")

# 购买设备-添加设备
def add_gmsb(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        ret = []
        try:
            ade_no = request.POST.get(u'de_no')

            ade_btime = datetime.strptime(request.POST.get(u'de_btime').encode("utf-8"),"%Y-%m-%d")
            ade_ptime = datetime.strptime(request.POST.get(u'de_ptime').encode("utf-8"),"%Y-%m-%d")

            bbuy_num = request.POST.get(u'buy_num')
            abuy_num = int(bbuy_num.encode("utf-8"))

            abeizhu = request.POST.get(u'beizhu')

            # print type(ade_no)
            # print type(ade_btime)
            # print type(ade_ptime)
            # print type(abuy_num)
            # print type(abeizhu)

            tt = device.objects.get(de_no=ade_no)
            tt.de_allnum = tt.de_allnum + abuy_num
            tt.de_lasnum = tt.de_lasnum + abuy_num
            tt.save()

            buy_device.objects.create(

                de_no=ade_no,
                de_btime=ade_btime,
                de_ptime=ade_ptime,
                buy_num=bbuy_num,
                beizhu=abeizhu,
            )
            tmp = {
                "stat": "1",
            }
            ret.append(tmp)
        except Exception,mmm:
            # print mmm
            # print "888"
            tmp = {
                "stat": "0",
            }
            ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")

# 借出设备
def jcsb(request):
    response = HttpResponseRedirect('/online/index/jcsb/')
    return render(request,'jcsb.html')

# 借出设备-获取设备
def get_jcsb(request):
    ans = []
    que = lend_device.objects.filter()
    for elem in que:
        mtime=elem.lend_date
        tmp={
            "lend_no": elem.lend_no,
            "de_no": elem.de_no,
            "st_no": elem.st_no,
            "lend_date": mtime.strftime("%Y-%m-%d"),
            "lend_num": elem.lend_num,
            "beizhu": elem.beizhu,
        }
        # print tmp
        ans.append(tmp)
    return HttpResponse(json.dumps(ans), content_type="application/json")

# 借出设备-编辑设备
def edit_jcsb(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        ret = []
        # print request.POST
        try:
            n_lend_no = request.POST.get(u'lend_no')
            n_de_no = request.POST.get(u'de_no')
            n_st_no = request.POST.get(u'st_no')
            n_lend_date = datetime.strptime(request.POST.get(u'lend_date'),"%Y-%m-%d")
            n_lend_num = request.POST.get(u'lend_num')
            n_beizhu = request.POST.get(u'beizhu')
            # print n_lend_no
            # print n_de_no
            # print n_st_no
            # print n_lend_date
            # print n_lend_num
            # print n_beizhu

            lend_device.objects.filter(lend_no=n_lend_no).delete()
            # print "删除"
            lend_device.objects.create(
                lend_no=int(n_lend_no),
                de_no=n_de_no,
                st_no=n_st_no,
                lend_date=n_lend_date,
                lend_num=int(n_lend_num),
                beizhu=n_beizhu,
            )
            # print "添加"
            tmp = {
                "stat": "1",
            }
            ret.append(tmp)
        except Exception,mmm:
            # print mmm
            # print "888"
            tmp = {
                "stat": "0",
            }
            ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")

# 借出设备-添加设备
def add_jcsb(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        ret = []
        try:
            ade_no = request.POST.get(u'de_no')
            ast_no = request.POST.get(u'st_no')
            alend_date = datetime.strptime(request.POST.get(u'lend_date').encode("utf-8"),"%Y-%m-%d")

            blend_num = request.POST.get(u'lend_num')
            alend_num = int(blend_num.encode("utf-8"))

            abeizhu = request.POST.get(u'beizhu')

            # print ade_no
            # print ast_no
            # print alend_date
            # print alend_num
            # print abeizhu
            # 员工存在
            ll = user.objects.get(st_username=ast_no)
            ll.st_age=ll.st_age
            # 设备存在
            tt = device.objects.get(de_no=ade_no)
            wan = tt.de_lasnum-alend_num
            if ( wan<0 ):
                tmp = {
                    "stat": "0",
                }
                ret.append(tmp)
            else :
                lend_device.objects.create(
                    de_no=ade_no,
                    st_no=ast_no,
                    lend_date=alend_date,
                    lend_num=blend_num,
                    beizhu=abeizhu,
                )

                tt.de_lasnum = tt.de_lasnum - alend_num
                tt.de_lennum = tt.de_lennum + alend_num
                tt.save()

                tmp = {
                    "stat": "1",
                }
                ret.append(tmp)
        except Exception,mmm:
            # print mmm
            # print "888"
            tmp = {
                "stat": "0",
            }
            ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")

# 损坏设备
def sbbx(request):
    response = HttpResponseRedirect('/online/index/sbbx/')
    return render(request,'sbbx.html')

# 损坏设备-获取设备
def get_sbbx(request):
    ans = []
    que = repair_device.objects.filter()
    for elem in que:
        mtime=elem.destroy_date
        tmp={
            "repair_no": elem.repair_no,
            "de_no": elem.de_no,
            "st_no": elem.st_no,
            "destroy_date": mtime.strftime("%Y-%m-%d"),
            "repair_num": elem.repair_num,
            "beizhu": elem.beizhu,
        }
        # print tmp
        ans.append(tmp)
    return HttpResponse(json.dumps(ans), content_type="application/json")

# 损坏设备-编辑设备
def edit_sbbx(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        ret = []
        # print request.POST
        try:
            n_repair_no = request.POST.get(u'repair_no')
            n_de_no = request.POST.get(u'de_no')
            n_st_no = request.POST.get(u'st_no')
            n_destroy_date = datetime.strptime(request.POST.get(u'destroy_date'),"%Y-%m-%d")
            n_repair_num = request.POST.get(u'repair_num')
            n_beizhu = request.POST.get(u'beizhu')
            print n_repair_no
            print n_de_no
            print n_st_no
            print n_destroy_date
            print n_repair_num
            print n_beizhu

            repair_device.objects.filter(repair_no=n_repair_no).delete()
            # print "删除"
            repair_device.objects.create(
                repair_no=int(n_repair_no),
                de_no=n_de_no,
                st_no=n_st_no,
                destroy_date=n_destroy_date,
                repair_num=int(n_repair_num),
                beizhu=n_beizhu,
            )
            # print "添加"
            tmp = {
                "stat": "1",
            }
            ret.append(tmp)
        except Exception,mmm:
            # print mmm
            # print "888"
            tmp = {
                "stat": "0",
            }
            ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")

# 损坏设备-添加设备
def add_sbbx(request):
    if request.COOKIES.get('username', '') != 'admin':
        response = HttpResponseRedirect('/online/index/')
        context = {}
        username = request.COOKIES.get('username', '')
        me = user.objects.get(st_username=username)
        context['username'] = me.st_name
        return render(request, 'index.html',context)
    else :
        ret = []
        try:
            ade_no = request.POST.get(u'de_no')
            ast_no = request.POST.get(u'st_no')
            adestroy_date = datetime.strptime(request.POST.get(u'destroy_date').encode("utf-8"),"%Y-%m-%d")

            brepair_num = request.POST.get(u'repair_num')
            arepair_num = int(brepair_num.encode("utf-8"))

            abeizhu = request.POST.get(u'beizhu')

            print ade_no
            print ast_no
            print adestroy_date
            print arepair_num
            print abeizhu
            # 员工存在
            ll = user.objects.get(st_username=ast_no)
            ll.st_age=ll.st_age
            # 设备存在
            tt = device.objects.get(de_no=ade_no)
            wan = tt.de_lasnum-arepair_num
            if ( wan<0 ):
                tmp = {
                    "stat": "0",
                }
                ret.append(tmp)
            else :
                repair_device.objects.create(
                    de_no=ade_no,
                    st_no=ast_no,
                    destroy_date=adestroy_date,
                    repair_num=brepair_num,
                    beizhu=abeizhu,
                )

                tt.de_lasnum = tt.de_lasnum - arepair_num
                tt.de_repnum = tt.de_repnum + arepair_num
                tt.save()

                tmp = {
                    "stat": "1",
                }
                ret.append(tmp)
        except Exception,mmm:
            # print mmm
            # print "888"
            tmp = {
                "stat": "0",
            }
            ret.append(tmp)
        return HttpResponse(json.dumps(ret), content_type="application/json")