from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    print('第一次')
    return HttpResponse('第一次')
