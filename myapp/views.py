from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
# Create your views here.

def page1(request):
    return HttpResponse("<h1>welcome to page 1</h1>")

def page2(request):
    return render(request,'page2.html',context={'data':"data is passed"})

def topic(request):
    d={'objects':Topic.objects.all()}
    return render(request,'page3.html',context=d)

def records(request):
    d={'objects':Access_Records.objects.order_by('date')}
    return render(request,'page4.html',context=d)

def page5(request):
    return render(request,'page5.html')

def display(request):
    data=request.POST.get('first_name',"Key not found")
    return HttpResponse("<h1>{}</h1>".format(data))









