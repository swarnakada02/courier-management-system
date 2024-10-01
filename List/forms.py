from django import forms
from .models import Listlist
class ListForm(forms.ModelForm):
    class Meta:
        model=Listlist
        fields=['receivername','sendername','pickupaddress','deliveryaddress','weight','cost']
