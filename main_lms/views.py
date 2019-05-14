from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q 
from django.contrib import messages
from django.http import *
from django.core.exceptions import ObjectDoesNotExist
import datetime
from datetime import date
from datetime import timedelta
from django import template
from main_lms.models import *
from main_lms.forms import *

# adminpanel(CRUD)
def viewslogin(request):
    return render(request,"accounts/login.html")
def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponse("Done...")
        else:  # form is not valid
            return HttpResponse("Form is not valid")
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)
def profile(request):
    args={'user':request.user}
    return render(request, 'accounts/profile.html', args)

#books
def binsert(request):  
    if request.method == "POST":  
        form = BookInsertForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                return redirect('/books/booklist')
            except:
                pass  
    else:
        form = BookInsertForm()  
    return render(request,'books/booksinsert.html',{'form':form})

def blist(request):  
    blist = BooksInsert.objects.order_by('bcreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
    context={
        'blist':blist,
    }
    return render(request,"books/bookslist.html",context)



# viewsforall (CRUD)
def viewshome(request):
    return render(request,"viewsforall/index.html")