"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index', views.home),
    # path('login', views.login),  # FBV
    path('login', views.LoginView.as_view()),  # CBV 根据get或者post提交自动找对应的类的方法

    # 参数
    path('person', views.person),
    path('book/<int:bid>', views.book),
    path('hobby', views.hobby),
    # 文件上传
    path('upload', views.upload),
    # mysql
    path('mysql', views.mysql),
    # JSON
    path('json', views.res_json),
]
