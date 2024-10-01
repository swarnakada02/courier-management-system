from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Branchlist 
from .forms import BranchForm

# Create your views here.
def Branch(request):
    data=Branchlist.objects.all()
    Branch={
        'data':data
    }
    return render(request,'Branch.html',context=Branch)
def add_branch(request):
    if request.method=='POST':
        forms=BranchForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('Branch')
    else:
        forms= BranchForm()
    return render (request,'add_branch.html', {'forms':forms})

    
