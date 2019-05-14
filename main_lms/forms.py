from django import forms  
from django.contrib.admin import widgets
from django.forms.widgets import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime
from main_lms.models import *

class BookInsertForm(forms.ModelForm):
    bid=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'book id'}),required=True,max_length=400)    
    bname= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'book name'}),required=True,max_length=400)
    btype = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'book type'}),required=True,max_length=400)
    bwriter=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'writer name'}),required=True,max_length=400)
    bquantity=  forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'1'}),required=True)    
    bshelf=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'shelf positon'}),required=True,max_length=400)
    #bquantity= forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','id':'sel'}, choices=Cat.objects.order_by('caty')),queryset=Cat.objects.order_by('caty'))    
    #ecat= forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','id':'sel'}, choices=Employee.objects.order_by('ename')),queryset=Employee.objects.order_by('ename'))    
    
    class Meta:  
        model = BooksInsert  
        fields = "__all__"