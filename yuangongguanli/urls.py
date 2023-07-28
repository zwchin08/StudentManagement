"""yuangongguanli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app01 import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    # 部门列表 记得导包from app01 import views
    path("depart/list/", views.depart_list),
    # 添加部门
    path("depart/add/", views.depart_add),
    # 删除部门
    path("depart/delete/", views.depart_delete),
    # 编辑 <ind:nid>是正则表达式转递id;意味着每次http://127.0.0.1:8000/depart/中间必须有数字/edit/
    path("depart/<int:nid>/edit/", views.depart_edit),

]
