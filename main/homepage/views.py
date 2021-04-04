from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'home.html')

def searchroom(request):
    return render(request,'searchroom.html')

def reserved(request):
    return render(request,'reserved.html')

def singleroom(request):
    return render(request,'singleroom.html')

