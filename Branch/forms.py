from django import forms
from .models import Branchlist
class BranchForm(forms.ModelForm):
    class Meta:
        model=Branchlist
        fields=['courierid','name','pincode','district','state','country'] 