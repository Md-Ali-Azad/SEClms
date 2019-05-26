from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.template import loader
import datetime
from datetime import date
from datetime import timedelta
from django import template
from main_lms.models import *
from main_lms.forms import *
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# adminpanel(CRUD)
def viewslogin(request):
	return render(request,"accounts/login.html")
def viewslogout(request):
	return render(request,"accounts/logout.html")


@login_required(login_url="/accounts/login/")
def activitylog(request):
	logs = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20]
	args = {'logs': logs}
	return render(request, 'setting/activitylog.html', args)



@login_required(login_url="/accounts/login/")
def register(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return  HttpResponse("Done...")
		else:  # form is not valid
			return HttpResponse("Form is not valid")
	else:
		form = UserCreationForm()

		args = {'form': form,'hcolor':hcolor,}
		return render(request, 'accounts/reg_form.html', args)
def profile(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	args={'user':request.user,'hcolor':hcolor,}
	return render(request, 'accounts/profile.html', args)






#books
def binsert(request):  
	hcolor=HeaderColor.objects.all()[:1].get()
	if request.method == "POST":  
		form = BookInsertForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				return redirect('/books/blist')
			except:
				pass  
	else:
		form = BookInsertForm() 
	args = {'form': form,'hcolor':hcolor,} 
	return render(request,'books/booksinsert.html',args)

def blist(request):
	hcolor=HeaderColor.objects.all()[:1].get()  
	blist = BooksInsert.objects.order_by('bcreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'blist':blist,
		'hcolor':hcolor
	}
	return render(request,"books/bookslist.html",context)
def bedit(request, id):  
	blist = BooksInsert.objects.get(id=id) 
	hcolor=HeaderColor.objects.all()[:1].get()
	form = BookInsertForm()
	context={
		'form': form,
		'blist':blist,
		'hcolor':hcolor,
	} 
	return render(request,'books/booksedit.html', context)

def bupdate(request, id): 
	hcolor=HeaderColor.objects.all()[:1].get() 
	blist = BooksInsert.objects.get(id=id)  
	form = BookInsertForm(request.POST, instance = blist)
	context={
		'blist':blist,
		'hcolor':hcolor,
	}
	if form.is_valid():  
		form.save()  
		return redirect("/books/blist")  
	return render(request, 'books/booksedit.html',context)
def bdelete(request, id):  
	blist = BooksInsert.objects.get(id=id)  
	blist.delete()  
	return redirect("/books/blist")

def bsearch(request):
	if request.method == "GET":
		search_text = request.GET['search_text']
		if search_text is not None and search_text != u"":
			search_text = request.GET['search_text']
			blist = BooksInsert.objects.filter(bname__contains = search_text)
		else:
			blist = []
	return render_to_response('search/bookssearch.html',{'blist' : blist})
#it worked ... editor problem -> sapce in to tab

#borrow
def brinsert(request):  
	if request.method == "POST":  
		form = BorrowInsertForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				return redirect('/borrow/brlist')
			except:
				pass  
	else:
		form = BorrowInsertForm() 
	args = {'form': form} 
	return render(request,'borrow/borrowinsert.html',args)

def brlist(request):
	brlist = BorrowInsert.objects.order_by('brdate').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'brlist':brlist,
	}
	return render(request,"borrow/borrowlist.html",context)



#students
def sinsert(request):  
	if request.method == "POST":  
		form = StuInsertForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				return redirect('/students/slist')
			except:
				pass  
	else:
		form =StuInsertForm() 
	args = {'form': form} 
	return render(request,'students/stuinsert.html',args)
def sedit(request, id):  
	slist = StuInsert.objects.get(id=id) 
	form = StuInsertForm()
	context={
		'form': form,
		'slist':slist,
	} 
	return render(request,'students/stuedit.html', context)

def supdate(request, id): 
	slist = StuInsert.objects.get(id=id)  
	form = StuInsertForm(request.POST, instance = slist)
	context={
		'slist':slist,
	}
	if form.is_valid():  
		form.save()  
		return redirect("/students/slist")  
	return render(request, 'students/stuedit.html',context)

def slist(request):
	slist = StuInsert.objects.order_by('screated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'slist':slist
	}
	return render(request,"students/stulist.html",context)

def sdelete(request, id):  
	slist = StuInsert.objects.get(id=id)  
	slist.delete()  
	return redirect("/students/slist")


#studentscategory
def cdepttype(request):
	if request.method == "POST":  
		form = StuDeptForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				return redirect('/cstudents/cdepttype')
			except:
				pass  
	else:
		form = StuDeptForm()  
	cdeptlist = StuDept.objects.order_by('cscreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'cdeptlist':cdeptlist,
		'form':form,
	}
	return render(request,"cstudents/studept.html",context)
def cdeptdelete(request, id):  
	cdeptlist = StuDept.objects.get(id=id)  
	cdeptlist.delete()  
	return redirect("/cstudents/cdepttype")

def csession(request):
	if request.method == "POST":  
		form = StuSessionForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				return redirect('/cstudents/csession')
			except:
				pass  
	else:
		form = StuSessionForm()  
	csession = StuSession.objects.order_by('cscreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'csession':csession,
		'form':form,
	}
	return render(request,"cstudents/stusession.html",context)
def csessiondelete(request, id):  
	csession = StuSession.objects.get(id=id)  
	csession.delete()  
	return redirect("/cstudents/csession")




#bookscategory
def cbtype(request):
	hcolor=HeaderColor.objects.all()[:1].get()  
	if request.method == "POST":  
		form = BooksTypeForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				return redirect('/cbooks/cbtype')
			except:
				pass  
	else:
		form = BooksTypeForm()  
	cbtlist = BooksType.objects.order_by('cbcreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'cbtlist':cbtlist,
		'form':form,
		'hcolor':hcolor,
	}
	return render(request,"cbooks/bookstype.html",context)
def cbdelete(request, id):  
	cbtlist = BooksType.objects.get(id=id)  
	cbtlist.delete()  
	return redirect("/cbooks/cbtype")

def cbshelf(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	if request.method == "POST":  
		form = BooksShelfForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				return redirect('/cbooks/cbshelf')
			except:
				pass  
	else:
		form = BooksShelfForm()  
	cbtlist = BooksShelf.objects.order_by('cbcreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'cbtlist':cbtlist,
		'form':form,
		'hcolor':hcolor,
	}
	return render(request,"cbooks/booksshelf.html",context)
def cbsdelete(request, id):  
	cbtlist = BooksShelf.objects.get(id=id)  
	cbtlist.delete()  
	return redirect("/cbooks/cbshelf")





# viewsforall (CRUD)
def viewshome(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	context={
		'hcolor':hcolor,
	}
	return render(request,"viewsforall/index.html", context)


#setting
def headercolor(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	context={
		'hcolor':hcolor,
	}
	return render(request,"setting/headercolor.html", context)
def chcolor(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	hcolor.hcolor=request.POST['hcolor']
	hcolor.save()
	context={
		'hcolor':hcolor,
	}
	return redirect('/setting/headercolor')
	return render(request,context)