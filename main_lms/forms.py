from django import forms  
from django.contrib.admin import widgets
from django.forms.widgets import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime
from main_lms.models import *
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsForm(forms.ModelForm):
    ntitle = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' News Title'}),required=True,max_length=500)
    ndetails= forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:  
        model = News  
        fields = "__all__"

class BookInsertForm(forms.ModelForm):
    bid=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'bid', 'placeholder':'book id'}),required=True,max_length=400)    
    bname= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'bname', 'placeholder':'book name'}),required=True,max_length=400)
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

class BorrowInsertForm(forms.ModelForm):
    attrs = {
            'class': "sel4",
            'id':'select'
        }
    sid=StuInsert.objects.values_list('sid', flat=True)
    locality_choices = [(e, e) for e in sid]
    brsid = forms.ChoiceField(choices=[(e, e) for e in sid],widget=Select(attrs=attrs),)
    #brsid = forms.ChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','class':'sel2','id':'inlineFormInputGroup'}, choices=locality_choices))
    brsname=  forms.ModelChoiceField(widget=forms.Select(attrs={'class':'sel5'}, choices=StuInsert.objects.order_by('sname')),queryset=StuInsert.objects.order_by('sname'))
    brbname=  forms.ModelChoiceField(widget=forms.Select(attrs={'class':'sel6'}, choices=BooksInsert.objects.order_by('bname')),queryset=BooksInsert.objects.order_by('bname'))
    
    brreturn= forms.DateField(initial=datetime.date.today(), widget=forms.DateInput(attrs={'id': 'datespan', 'class':'seldate'}))
    class Meta:  
        model = BorrowInsert  
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



#proble solved
'''


I had the same problem, my solution now is to use the ChoiceField instead of the ModelChoiceField. I believe this makes sense, since we do not want the user to select model instances, but distinct attribute values throughout one table column and the same attribute might well correspond to several model instances.

class SearchForm(forms.Form):
    # get the distinct attributes from one column
    entries = Locality.objects.values_list('islandgroup', flat=True).distinct('islandgroup')
    # change the entries to a valid format for choice field
    locality_choices = [(e, e) for e in entries]
    # the actual choice field
    island_group = forms.ChoiceField(
        required=False,
        choices=locality_choices)

This way Django's inbuilt validation performs exactly what we want, i.e. checking whether a member of the set of all possible attributes from one column was selected.

'''