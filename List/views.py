from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Listlist
from .forms import ListForm

# Create your views here.
def List(request):
    data=Listlist.objects.all()
    print(data)
    List={
        'data':data
    }
    return render(request,'List.html',context=List)
def add_list(request):
    if request.method=='POST':
        forms=ListForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('List')
    else:
        forms= ListForm()
    return render(request,'add_list.html', {'forms':forms})


