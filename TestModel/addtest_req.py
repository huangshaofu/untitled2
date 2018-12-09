from django.shortcuts import render
from django.views.decorators import csrf
from TestModel.models import Test

# 接收POST请求数据
def addtest_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['name']
        ctx['rlt2'] = request.POST['password']
        # 数据库操作
        test1 = Test(name=ctx['rlt'],password=ctx['rlt2'])
        test1.save()
        ctx['rlt3']='chengg'
    #return render(request, "TestModel/addtest.html", ctx)
    return render(request, "addtest.html", ctx)