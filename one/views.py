from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    print('第一次')
    return HttpResponse('第一次')
def user(request):
    print('user视图')
    return HttpResponse('访问user视图')
def ceshi(request):
    print('视图提交')
    return HttpResponse('配置好之后的第一次视图提交方式---码云仓库 github仓库码云设置,所以此时直接用不了',)


