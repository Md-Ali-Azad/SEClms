from django import forms  
from django.contrib.admin import widgets
from django.forms.widgets import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime
from main_lms.models import *

class BookInsertForm(forms.ModelForm):
    bid=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'inlineFormInputGroup', 'placeholder':'book id'}),required=True,max_length=400)    
    bname= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'book name'}),required=True,max_length=400)
    btype = forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','class':'sel','id':'inlineFormInputGroup'}, choices=BooksType.objects.order_by('cbtype')),queryset=BooksType.objects.order_by('cbtype'))
    bwriter=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'writer name'}),required=True,max_length=400)
    bquantity=  forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'1'}),required=True)    
    bshelf=  forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','class':'sel','id':'inlineFormInputGroup'}, choices=BooksShelf.objects.order_by('cbshelf')),queryset=BooksShelf.objects.order_by('cbshelf'))
    #bquantity= forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','id':'sel'}, choices=Cat.objects.order_by('caty')),queryset=Cat.objects.order_by('caty'))    
    #ecat= forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','id':'sel'}, choices=Employee.objects.order_by('ename')),queryset=Employee.objects.order_by('ename'))    
    
    class Meta:  
        model = BooksInsert  
        fields = "__all__"

class StuInsertForm(forms.ModelForm):
    gender = (
        ('M', 'Male',),
        ('F', 'Female',),
        ('T', 'Transgender',),
    )
    sid=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'inlineFormInputGroup', 'placeholder':'Reg. id'}),required=True,max_length=400)    
    sname= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Student name'}),required=True,max_length=400)
    sdept = forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','class':'sel','id':'inlineFormInputGroup'}, choices=StuDept.objects.order_by('cdept')),queryset=StuDept.objects.order_by('cdept'))
    ssession = forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','class':'sel','id':'inlineFormInputGroup'}, choices=StuSession.objects.order_by('csession')),queryset=StuSession.objects.order_by('csession'))    
    saddress=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),required=True,max_length=400)
    scontact=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact'}),required=True,max_length=400)    
    semail=  forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),required=True,max_length=400)    
    sgender=  forms.CharField(widget=forms.Select(attrs={'data-style':'btn-primary','class':'sel2','id':'inlineFormInputGroup'}, choices=gender))        
    
    class Meta:  
        model = StuInsert  
        fields = "__all__"

class BooksTypeForm(forms.ModelForm):
    cbtype = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'inlineFormInputGroup', 'placeholder':'book type'}),required=True,max_length=400)
    class Meta:  
        model = BooksType  
        fields = "__all__"

class BooksShelfForm(forms.ModelForm):
    cbshelf = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'book shelf', 'value':'A-00 (Room-300)'}),required=True,max_length=400)
    class Meta:  
        model = BooksShelf  
        fields = "__all__"


class StuDeptForm(forms.ModelForm):
    cdept = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'inlineFormInputGroup', 'placeholder':'Dept.'}),required=True,max_length=400)
    class Meta:  
        model = StuDept  
        fields = "__all__"

class StuSessionForm(forms.ModelForm):
    csession = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'session', 'value':'2015-16'}),required=True,max_length=400)
    class Meta:  
        model = StuSession  
        fields = "__all__"
#class HeaderColor(forms.ModelForm):
#    hcolor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'book shelf', 'value':'A-00 (Room-300)'}),required=True,max_length=400)
#    class Meta:  
#        model = BooksShelf  
#        fields = "__all__"