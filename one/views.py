from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    print('第一次')
    return HttpResponse('第一次')
def user(request):
    print('user视图')
    return HttpResponse('访问user视图')
