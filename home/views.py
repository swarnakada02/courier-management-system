from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('home')
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')

# Create your views here.
