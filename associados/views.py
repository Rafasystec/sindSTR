from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{'title':'Painel'})

def login(request):
    return render(request,'login.html',{'title':'Login'})

def register(request):
    return render(request,'register.html',{'title':'Register'})
