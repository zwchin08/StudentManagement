from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def depart_list(request):
    """部门列表"""
    # 1.去数据库中获取所有的部门列表
    queryset = models.Department.objects.all()

    return render(request, "depart_list.html", {"queryset": queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, "depart_add.html")

    # 获取post提交的数据(title输入为空)
    title = request.POST.get("title")
    # 获取完的数据保存到数据库
    models.Department.objects.create(title=title)
    # 重定向回到部门列表页面
    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""
    """
    1.其实删除的时候也可以选择用post额形式输入要删除的部门然后在删除，那时候的情形时上边只有一个新建按钮和一个删除的按钮
    2.下面使用的是GET形式，这样就不用在创建一个删除页面了
    """
    # 获取id
    nid = request.GET.get("nid")
    # 删除
    models.Department.objects.filter(id=nid).delete()
    # 跳转回部门列表界面
    return redirect("/depart/list/")


#   path("depart/<int:nid>/edit/", views.depart_edit);所以下面(request,nid):多传了一个nid
def depart_edit(request, nid):
    """编辑修改部门"""
    if request.method == "GET":
        # 根据nid就可以获取对应的部门信息,=>获取要编辑的那一行对象
        row_obj = models.Department.objects.filter(id=nid).first()
        # 拿到对象后可以使用点.来获取对应的对象的字段
        # print(row_obj.id, row_obj.title)
        # 使用"row_obj":row_obj}把对象row_obj当作参数传到模板中，在模板中直接拿到对象就可获取对应的对象的字段
        return render(request, "depart_edit.html", {"row_obj": row_obj})

    # 拿到用户在编辑的页面进行编辑后的数据==>用户提交的标题
    title = request.POST.get("title")
    # 根基用户的id=>然后把拿到的数据在数据库进行更新  ,如果有多个字段则update(title=title，name="",....)
    models.Department.objects.filter(id=nid).update(title=title)
    # 更新完后，跳转回部门列表界面
    return redirect("/depart/list/")
