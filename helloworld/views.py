from django.shortcuts import render, HttpResponse, redirect
# CBV 需要导入包
from django.views import View

# JSON
from django.http.response import JsonResponse
# import pymysql

# DB
from . import db


# request--environ 请求相关数据，request叫做HTTPRequest对象,请求的相关数据都是request属性。这个参数是必要的
def home(request):
    # render渲染模板文件,django会自动去templates目录下寻找文件
    # print(request.method) # GET
    print(request.META)
    context = {
        'title': test(),
        'flag': True,
        'lists': ['苹果', '香蕉', '雪梨', '葡萄']
    }
    return render(request, 'index.html', context)


# FBV
# def login(request):
#     # 判断请求方式
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         # post提交过来的参数
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # print(username, password)
#         if username == 'root' and password == 'root':
#             # response 响应头
#             res = render(request, 'admin.html')
#             # 添加响应头键值对
#             res['test'] = 'test response'
#             # 设置http状态码
#             # res.status_code = 404
#             return res
#         else:
#             # 在django中，return字符串需要HttpResponse
#             return HttpResponse('用户名或者密码错误！')


# 参数
def person(request):
    # get
    uid = request.GET.get('uid')
    name = request.GET.get('name')

    data = {
        'id': uid,
        'name': name
    }
    # return HttpResponse('姓名：' + name + 'id：' + uid)
    return JsonResponse(data)


def book(request, bid):
    return HttpResponse('参数：{}'.format(bid))


def hobby(request):
    # post
    if request.method == 'GET':
        return render(request, 'hobby.html')
    else:
        print('********表单提交********')
        username = request.POST.get('username')
        print(username)
        print(request.POST.get('sex'))
        # 获取提交过来的多项，要用getlist()
        print(request.POST.getlist('hobby'))

        # 重定向
        if username == 'root':
            # 封装了302状态码
            return redirect('/index')

        return HttpResponse('已提交!')


# 文件上传
def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        print('文件上传')
        # 文件句柄
        file = request.FILES.get('file')
        # 获取文件名
        print(file.name)

        with open('upload/' + file.name, 'wb') as f:
            for i in file:
                f.write(i)

        return HttpResponse('ok')


# CBV
# 把上面的FBV改写成如下
class LoginView(View):
    # get请求，获取login页面
    def get(self, request):
        return render(request, 'login.html')

    # post请求，获取post提交的数据，并校验等处理
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'root' and password == 'root':
            res = render(request, 'admin.html')
            res['test'] = 'class based view'
            return res
        else:
            return HttpResponse('用户名或者密码错误！')


# mysql
def mysql(request):
    '''
    db = pymysql.connect(host='localhost', user='root', password='root', database='flask_shopping')
    # sql = 'show tables'
    sql = 'SELECT * FROM goods'
    # sql = 'SELECT * FROM goods WHERE id = 4'
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print('********MYSQL********')
    # print(result)
    '''
    result = db.get_all_goods()

    context = {
        'data': result
    }

    # 关闭数据库连接
    # cursor.close()

    return render(request, 'mysql.html', context)


# JSON
def res_json(request):
    data = {
        'patient_name': '张三',
        'age': '25',
        'patient_id': '19000347',
        '诊断': '上呼吸道感染',
    }

    return JsonResponse(data)


# function
def test():
    return 'hello Django!'
