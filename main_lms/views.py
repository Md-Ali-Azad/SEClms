from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import HttpResponse, Http404, get_object_or_404
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
from django.db import connection
from django.db.models import F
from django.db import transaction
from django.db.models import Sum, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#newspanel
@login_required(login_url="/accounts/login/")
def news(request):
	if request.method == "POST":  
		form = NewsForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				messages.success(request, 'New Post is Added successfully')
				return redirect('/news/news')
			except:
				pass
				
	else:
		form = NewsForm()
		
	nlist = News.objects.order_by('ncreated_at').reverse()   
	paginator = Paginator(nlist, 3) 
	page = request.GET.get('page')
	nlist_show = paginator.get_page(page)
	args={'news': 'active', 'form': form, 'nlist':nlist, 'nlist_show': nlist_show}
	return render(request, "news/news.html", args)

@login_required(login_url="/accounts/login/")
def ndelete(request, id):  
	nlist = News.objects.get(id=id)  
	nlist.delete()  
	messages.warning(request, 'Post is deleted successfully')
	return redirect("/news/news")
@login_required(login_url="/accounts/login/")
def nedit(request, id):  
	post = get_object_or_404(News, id=id)
	form = NewsForm(request.POST or None, request.FILES or None, instance=post)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Post is updated successfully')
		return redirect('/news/news')
	return render(request, 'news/newsedit.html', {"form": form,'news': 'active'})
def newscomments(request, id):
	nlist = News.objects.get(id=id)
	return render(request,'news/newscomments.html', {'nlist':nlist, 'news': 'active'})



	# adminpanel(CRUD)
def viewslogin(request):
	args={'log': 'active', 'hello':'e'}
	return render(request,"accounts/login.html", args)
def viewslogout(request):
	return render(request,"accounts/logout.html")


@login_required(login_url="/accounts/login/")
def activitylog(request):
	logs = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20]
	args = {'logs': logs, 'setlog':'active', 'set':'active'}
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

		args = {'form': form,'hcolor':hcolor, 'reg':'active', 'set':'active'}
		return render(request, 'accounts/reg_form.html', args)
def profile(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	args={'user':request.user,'hcolor':hcolor, 'setpro':'active', 'set':'active'}
	return render(request, 'accounts/profile.html', args)






#books
@login_required(login_url="/accounts/login/")
def binsert(request):  
	hcolor=HeaderColor.objects.all()[:1].get()
	if request.method == "POST":  
		form = BookInsertForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				messages.success(request, 'List is Added successfully')
				return redirect('/books/blist')
			except:
				pass  
	else:
		form = BookInsertForm() 
	args = {'form': form,'hcolor':hcolor, 'b':'active', 'bin':'active'} 
	return render(request,'books/booksinsert.html',args)

@login_required(login_url="/accounts/login/")
def blist(request):
	blist = BooksInsert.objects.order_by('bcreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	totalb= BooksInsert.objects.aggregate(Sum('bquantity'))
	context={
		'blist':blist,
		'totalb':totalb,
		'b':'active', 'bli':'active'
	}
	return render(request,"books/bookslist.html",context)

@login_required(login_url="/accounts/login/")
def bedit(request, id):  
	blist = BooksInsert.objects.get(id=id) 
	hcolor=HeaderColor.objects.all()[:1].get()
	form = BookInsertForm()
	context={
		'form': form,
		'blist':blist,
		'hcolor':hcolor,
		'b':'active'
	} 
	return render(request,'books/booksedit.html', context)

@login_required(login_url="/accounts/login/")
def bupdate(request, id): 
	hcolor=HeaderColor.objects.all()[:1].get() 
	blist = BooksInsert.objects.get(id=id)  
	form = BookInsertForm(request.POST, instance = blist)
	context={
		'blist':blist,
		'hcolor':hcolor,
		'b':'active'
	}
	if form.is_valid():  
		form.save()
		messages.success(request, 'List is updated successfully')  
		return redirect("/books/blist")  
	return render(request, 'books/booksedit.html',context)

@login_required(login_url="/accounts/login/")
def bdelete(request, id):  
	blist = BooksInsert.objects.get(id=id)  
	blist.delete()
	messages.warning(request, 'List is deleted successfully')  
	return redirect("/books/blist")

def bsearch(request):
	if request.user.is_authenticated:
		tem=['search/bookssearch.html']
	else:
		tem=['viewsforall/bookssearch.html']
	if request.method == "GET":
		search_text = request.GET['search_text']
		if search_text is not None and search_text != u"":
			search_text = request.GET['search_text']
			blist = BooksInsert.objects.filter(bname__contains = search_text)
		else:
			blist = []
	return render_to_response(tem,{'blist' : blist})
#booksmatchinginfo
def bsearch_m_info(request):
	if request.user.is_authenticated:
		tem=['matching_info/booksearch_id_name.html']
	if request.method == "GET":
		search_textbm = request.GET['search_textbm']
		if search_textbm is not None and search_textbm != u"":
			search_textbm = request.GET['search_textbm']
			blist = BooksInsert.objects.filter(Q(bname__icontains = search_textbm) | Q(bid__icontains = search_textbm))
		else:
			blist = []
	return render_to_response(tem,{'blist' : blist})

def btsearch(request):
	if request.user.is_authenticated:
		tem=['search/bookssearchbt.html']
	else:
		tem=['viewsforall/bookssearchbt.html']
	if request.method == "GET":
		search_textbt = request.GET['search_textbt']
		if search_textbt is not None and search_textbt != u"":
			search_textbt = request.GET['search_textbt']
			blist = BooksInsert.objects.filter(btype__contains = search_textbt)
		else:
			blist = []
	return render_to_response(tem,{'blist' : blist})
def ballsearch(request):
	if request.user.is_authenticated:
		tem=['search/bookssearchall.html']
	else:
		tem=['viewsforall/bookssearchall.html']
	if request.method == "GET":
		search_textball = request.GET['search_textball']
		if search_textball is not None and search_textball != u"":
			search_textball = request.GET['search_textball']
			blist = BooksInsert.objects.filter(Q(bname__icontains = search_textball) | Q(btype__icontains = search_textball) |Q(bwriter__icontains = search_textball) | Q(bshelf__icontains = search_textball) | Q(bcreated_at__icontains = search_textball)| Q(bquantity__icontains = search_textball) | Q(bid__icontains = search_textball) )
		else:
			blist = []
	return render_to_response(tem,{'blist' : blist})
#it worked ... editor problem -> sapce in to tab

#borrow
@login_required(login_url="/accounts/login/")
def brinsert(request):
	blist = BooksInsert.objects.all()
	if request.method == "POST":  
		form = BorrowInsertForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				answer = form.cleaned_data['brbname']
				idd = BooksInsert.objects.get(bname=answer)
				#print(answer)
				BooksInsert.objects.filter(id=idd.id).update(bquantity=F('bquantity') - 1)
				messages.success(request, 'List is Added successfully')
				return redirect('/borrow/brlist')
			except:
				pass  
	else:
		form = BorrowInsertForm() 
	args = {'form': form, 'br':'active', 'brin':'active'} 
	#if request.GET.get('brsub'):        #not working
		#with transaction.atomic():
			#BooksInsert.objects.filter(id=18).update(bquantity=F('bquantity') - x)
	return render(request,'borrow/borrowinsert.html',args)

@login_required(login_url="/accounts/login/")
def brlist(request):
	slist = StuInsert.objects.all()
	blist = BooksInsert.objects.all()
	brlist = BorrowInsert.objects.order_by('brdate').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'brlist':brlist,'slist':slist, 'blist':blist, 'br':'active', 'brli':'active'
	}
	return render(request,"borrow/borrowlist.html",context)

@login_required(login_url="/accounts/login/")
def bredit(request, id):  
	brlist = BorrowInsert.objects.get(id=id) 
	form = BorrowInsertForm()
	context={
		'form': form,
		'brlist':brlist,
		'br':'active'
	} 
	return render(request,'borrow/borrowedit.html', context)


@login_required(login_url="/accounts/login/")
def brupdate(request, id): 
	brlist = BorrowInsert.objects.get(id=id)  
	form = BorrowInsertForm(request.POST, instance = brlist)
	context={
		'brlist':brlist,
	}
	if form.is_valid():  
		form.save()
		messages.success(request, 'List is updated successfully')  
		return redirect("/borrow/brlist")  
	return render(request, 'borrow/borrowedit.html',context)

@login_required(login_url="/accounts/login/")
def brdelete(request, id):
	brlist = BorrowInsert.objects.get(id=id)
	BooksInsert.objects.filter(bname=brlist.brbname).update(bquantity=F('bquantity') + 1)
	messages.warning(request, 'List is deleted successfully')  
	brlist.delete()  
	return redirect("/borrow/brlist")
def brnsearch(request):
	slist = StuInsert.objects.all()
	blist = BooksInsert.objects.all()
	if request.user.is_authenticated:
		tem=['search/brsearchbrn.html']
	else:
		tem=['viewsforall/brsearchbrn.html']
	if request.method == "GET":
		search_textbrn = request.GET['search_textbrn']
		if search_textbrn is not None and search_textbrn != u"":
			search_textbrn = request.GET['search_textbrn']
			brlist = BorrowInsert.objects.filter(Q(brsname__icontains = search_textbrn) | Q(brsid__icontains = search_textbrn))
		else:
			brlist = []
	context={
		'brlist':brlist,
		'slist': slist,
		'blist': blist
	} 
	return render_to_response(tem,context)
def brbdsearch(request):
	slist = StuInsert.objects.all()
	blist = BooksInsert.objects.all()
	if request.user.is_authenticated:
		tem=['search/brsearchbrbd.html']
	else:
		tem=['viewsforall/brsearchbrbd.html']
	if request.method == "GET":
		search_textbrbd = request.GET['search_textbrbd']
		if search_textbrbd is not None and search_textbrbd != u"":
			search_textbrbd = request.GET['search_textbrbd']
			brlist = BorrowInsert.objects.filter(Q(brbname__contains = search_textbrbd) | Q(brreturn__contains = search_textbrbd) | Q(brdate__contains = search_textbrbd))
		else:
			brlist = []
	context={
		'brlist':brlist,
		'slist': slist,
		'blist': blist
	} 
	return render_to_response(tem,context)

#students
@login_required(login_url="/accounts/login/")
def sinsert(request):  
	if request.method == "POST":  
		form = StuInsertForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				messages.success(request, 'List is Added successfully')
				return redirect('/students/slist')
			except:
				pass  
	else:
		form =StuInsertForm() 
	args = {'form': form, 's':'active', 'sin':'active'} 
	return render(request,'students/stuinsert.html',args)

@login_required(login_url="/accounts/login/")
def sedit(request, id):  
	slist = StuInsert.objects.get(id=id) 
	form = StuInsertForm()
	context={
		'form': form,
		'slist':slist,
		's':'active',
	} 
	return render(request,'students/stuedit.html', context)


@login_required(login_url="/accounts/login/")
def supdate(request, id): 
	slist = StuInsert.objects.get(id=id)  
	form = StuInsertForm(request.POST, instance = slist)
	context={
		'slist':slist,
	}
	if form.is_valid():  
		form.save() 
		messages.success(request, 'List is updated successfully') 
		return redirect("/students/slist")  
	return render(request, 'students/stuedit.html',context)


@login_required(login_url="/accounts/login/")
def slist(request):
	slist = StuInsert.objects.order_by('screated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'slist':slist, 's':'active', 'sli':'active'
	}
	return render(request,"students/stulist.html",context)


@login_required(login_url="/accounts/login/")
def sdelete(request, id):  
	slist = StuInsert.objects.get(id=id)  
	slist.delete()
	messages.warning(request, 'List is deleted successfully')  
	return redirect("/students/slist")

#booksmatchinginfo
def ssearch_m_info(request):
	if request.user.is_authenticated:
		tem=['matching_info/stusearch_id_name.html']
	if request.method == "GET":
		search_textsm = request.GET['search_textsm']
		if search_textsm is not None and search_textsm != u"":
			search_textsm = request.GET['search_textsm']
			slist = StuInsert.objects.filter(Q(sname__icontains = search_textsm) | Q(sid__icontains = search_textsm))
		else:
			slist = []
	return render_to_response(tem,{'slist' : slist})

def snsearch(request):
	if request.user.is_authenticated:
		tem=['search/studentssearchsn.html']
	else:
		tem=['viewsforall/studentssearchsn.html']
	if request.method == "GET":
		search_textsn = request.GET['search_textsn']
		if search_textsn is not None and search_textsn != u"":
			search_textsn = request.GET['search_textsn']
			slist = StuInsert.objects.filter(Q(sname__icontains = search_textsn) | Q(sid__icontains = search_textsn))
		else:
			slist = []
	return render_to_response(tem,{'slist' : slist})
def sdsearch(request):
	if request.user.is_authenticated:
		tem=['search/studentssearchsd.html']
	else:
		tem=['viewsforall/studentssearchsd.html']
	if request.method == "GET":
		search_textsd = request.GET['search_textsd']
		if search_textsd is not None and search_textsd != u"":
			search_textsd = request.GET['search_textsd']
			slist = StuInsert.objects.filter(Q(sdept__icontains = search_textsd) | Q(ssession__icontains = search_textsd))
		else:
			slist = []
	return render_to_response(tem,{'slist' : slist})
def sallsearch(request):
	if request.user.is_authenticated:
		tem=['search/studentssearchsall.html']
	else:
		tem=['viewsforall/studentssearchsall.html']
	if request.method == "GET":
		search_textsall = request.GET['search_textsall']
		if search_textsall is not None and search_textsall != u"":
			search_textsall = request.GET['search_textsall']
			slist = StuInsert.objects.filter(Q(sname__icontains = search_textsall) | Q(sdept__icontains = search_textsall) |Q(ssession__icontains = search_textsall) | Q(scontact__icontains = search_textsall) | Q(screated_at__icontains = search_textsall)| Q(saddress__icontains = search_textsall) | Q(sid__icontains = search_textsall) | Q(semail__icontains = search_textsall) | Q(sgender__icontains = search_textsall))
		else:
			slist = []
	return render_to_response(tem,{'slist' : slist})

#studentscategory
@login_required(login_url="/accounts/login/")
def cdepttype(request):
	if request.method == "POST":  
		form = StuDeptForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				messages.success(request, 'List is Added successfully')
				return redirect('/cstudents/cdepttype')
			except:
				pass  
	else:
		form = StuDeptForm()  
	cdeptlist = StuDept.objects.order_by('cscreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'cdeptlist':cdeptlist,
		'form':form,
		's':'active', 'sd':'active'
	}
	return render(request,"cstudents/studept.html",context)

@login_required(login_url="/accounts/login/")
def cdeptdelete(request, id):  
	cdeptlist = StuDept.objects.get(id=id)  
	cdeptlist.delete()
	messages.warning(request, 'List is deleted successfully')  
	return redirect("/cstudents/cdepttype")


@login_required(login_url="/accounts/login/")
def csession(request):
	if request.method == "POST":  
		form = StuSessionForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				messages.success(request, 'List is Added successfully')
				return redirect('/cstudents/csession')
			except:
				pass  
	else:
		form = StuSessionForm()  
	csession = StuSession.objects.order_by('cscreated_at').reverse()   #created_at desc order  #reverse() for implied the Asc
	context={
		'csession':csession,
		'form':form,
		's':'active', 'ss':'active'
	}
	return render(request,"cstudents/stusession.html",context)

@login_required(login_url="/accounts/login/")
def csessiondelete(request, id):  
	csession = StuSession.objects.get(id=id)  
	csession.delete() 
	messages.warning(request, 'List is deleted successfully') 
	return redirect("/cstudents/csession")




#bookscategory
@login_required(login_url="/accounts/login/")
def cbtype(request):
	hcolor=HeaderColor.objects.all()[:1].get()  
	if request.method == "POST":  
		form = BooksTypeForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				messages.success(request, 'List is Added successfully')
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
		'b':'active', 'bt':'active'
	}
	return render(request,"cbooks/bookstype.html",context)

@login_required(login_url="/accounts/login/")
def cbdelete(request, id):  
	cbtlist = BooksType.objects.get(id=id)  
	cbtlist.delete()  
	messages.warning(request, 'List is deleted successfully')
	return redirect("/cbooks/cbtype")


@login_required(login_url="/accounts/login/")
def cbshelf(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	if request.method == "POST":  
		form = BooksShelfForm(request.POST)  
		if form.is_valid():  
			try:
				form.save()
				messages.success(request, 'List is Added successfully')
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
		'b':'active', 'bs':'active'
	}
	return render(request,"cbooks/booksshelf.html",context)

@login_required(login_url="/accounts/login/")
def cbsdelete(request, id):  
	cbtlist = BooksShelf.objects.get(id=id)  
	cbtlist.delete()
	messages.warning(request, 'List is deleted successfully')
	return redirect("/cbooks/cbshelf")





# viewsforall (CRUD)
def viewsnews(request):
	nlist = News.objects.order_by('ncreated_at').reverse()   
	paginator = Paginator(nlist, 3) 
	page = request.GET.get('page')
	nlist_show = paginator.get_page(page)
	args={'news': 'active','nlist':nlist, 'nlist_show': nlist_show}
	return render(request,"viewsforall/news.html", args)

def viewshome(request):
	form=SortForm()
	today = BorrowInsert.objects.filter(brreturn=datetime.date.today()).order_by('brreturn')
	flist = BorrowInsert.objects.filter(brreturn__lt=datetime.date.today()).order_by('brreturn')
	upcoming = BorrowInsert.objects.filter(brreturn__range=(datetime.date.today()+timedelta(days=1) ,datetime.date.today()+timedelta(days=7))).order_by('brreturn') 
	slist = StuInsert.objects.all()
	blist = BooksInsert.objects.all()
	fieldname='brbname'
	fieldname2='brsname'
	topb=BorrowInsert.objects.values(fieldname).annotate(count=Count(fieldname)).order_by('-count')[0:10]  #first 10 for last 10 [-:10]
	tops=BorrowInsert.objects.values(fieldname2).annotate(count=Count(fieldname2)).order_by('-count')[0:10]
	if request.method == "POST":  
		form = SortForm(request.POST)  
		if form.is_valid():  
			try:
				answer = form.cleaned_data['sort']
				today = BorrowInsert.objects.filter(brreturn=datetime.date.today()).order_by(answer)
				flist = BorrowInsert.objects.filter(brreturn__lt=datetime.date.today()).order_by(answer)
				upcoming = BorrowInsert.objects.filter(brreturn__range=(datetime.date.today()+timedelta(days=1) ,datetime.date.today()+timedelta(days=7))).order_by(answer) 
				#print(answer)
				msg=''
				if answer=='brreturn':
					msg='Retrun Date'
				elif answer=='brdate':
					msg='Borrow Date'
				elif answer=='brsid':
					msg='Student ID'
				else:
					pass
				messages.success(request, 'Lists are Sorted by %s asc.' % msg)
			except:
				pass  
	else:
		form=SortForm()
	context={
		'today':today, 'flist':flist,'slist': slist,
		'blist': blist, 'upcoming':upcoming, 'h':'active', 'hh':'active', 'form':form,
		'topb' : topb, 'tops' : tops
	}
	return render(request,"viewsforall/index.html", context)
# Retrun a book ()
def rtbooks(request):
	slist = StuInsert.objects.all()
	blist = BooksInsert.objects.all()  
	if request.method == "GET":
		search_textrt = request.GET['search_textrt']
		if search_textrt is not None and search_textrt != u"":  #u means unicode
			search_textrt = request.GET['search_textrt']
			today = BorrowInsert.objects.filter( Q(brsname__icontains = search_textrt) | Q(brsid__icontains = search_textrt), brreturn=datetime.date.today())
			flist = BorrowInsert.objects.filter(Q(brsname__icontains = search_textrt) | Q(brsid__icontains = search_textrt) , brreturn__lt=datetime.date.today())
			upcoming = BorrowInsert.objects.filter(Q(brsname__icontains = search_textrt) | Q(brsid__icontains = search_textrt), brreturn__range=(datetime.date.today()+timedelta(days=1) ,datetime.date.today()+timedelta(days=7))).order_by('brreturn') 
			brlist = BorrowInsert.objects.filter(Q(brsname__icontains = search_textrt) | Q(brsid__icontains = search_textrt)).order_by('brreturn')
		else:
			today = []
			flist = []
			upcoming = []
			brlist = []
	context={
		'flist':flist, 'slist':slist, 'blist':blist,'upcoming':upcoming, 'today':today, 'brlist':brlist
	}
	return render_to_response('search/booksreturn.html',context)
##sql query practice
def brdetails(request):
	slist = StuInsert.objects.all()
	blist = BooksInsert.objects.all()
	cursor = connection.cursor()    
	cursor.execute("select * , cast((julianday('now') - julianday(brreturn)) as int)*10 as df from BorrowInsert where brreturn < current_date order by brreturn")
	results = cursor.fetchall()

	x = cursor.description
	resultsList = []   
	for r in results:
		i = 0
		d = {}
		while i < len(x):
			d[x[i][0]] = r[i]
			i = i+1
		resultsList.append(d)
	
	cursor = connection.cursor()    
	cursor.execute("select *  from BorrowInsert where brreturn = current_date")
	
	results = cursor.fetchall()

	x = cursor.description
	resultsList1 = []   
	for r in results:
		i = 0
		d = {}
		while i < len(x):
			d[x[i][0]] = r[i]
			i = i+1
		resultsList1.append(d)
	context={
		"to":resultsList,
		'tt':resultsList1,
		'slist': slist,
		'blist': blist
	} 
	return render(request,"viewsforall/index.html", context)


#Home page
def isearch(request):
	slist = StuInsert.objects.all()
	blist = BooksInsert.objects.all()  
	if request.method == "GET":
		search_texti = request.GET['search_texti']
		if search_texti is not None and search_texti != u"":
			search_texti = request.GET['search_texti']
			today = BorrowInsert.objects.filter( Q(brsname__icontains = search_texti) | Q(brsid__icontains = search_texti), brreturn=datetime.date.today())
			flist = BorrowInsert.objects.filter(Q(brsname__icontains = search_texti) | Q(brsid__icontains = search_texti) , brreturn__lt=datetime.date.today())
			upcoming = BorrowInsert.objects.filter(Q(brsname__icontains = search_texti) | Q(brsid__icontains = search_texti), brreturn__range=(datetime.date.today()+timedelta(days=1) ,datetime.date.today()+timedelta(days=7))).order_by('brreturn') 
	
		else:
			today = []
			flist = []
			upcoming = []
	context={
		'flist':flist, 'slist':slist, 'blist':blist,'upcoming':upcoming, 'today':today
	}
	return render_to_response('viewsforall/indexsearch.html',context)


#books and sutdent details
def studetails(request, id):
	if request.user.is_authenticated:
		tem=['students/studetails.html']
	else:
		tem=['viewsforall/studetails.html']  
	slist = StuInsert.objects.get(id=id) 
	context={
		'slist':slist,
	} 
	return render(request,tem, context)

def booksdetails(request, id):  
	blist = BooksInsert.objects.get(id=id) 
	context={
		'blist':blist,
	} 
	return render(request,'viewsforall/booksdetails.html', context)

#setting
@login_required(login_url="/accounts/login/")
def headercolor(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	context={
		'hcolor':hcolor,'setcolor':'active', 'set':'active'
	}
	return render(request,"setting/headercolor.html", context)
@login_required(login_url="/accounts/login/")
def chcolor(request):
	hcolor=HeaderColor.objects.all()[:1].get()
	hcolor.hcolor=request.POST['hcolor']
	hcolor.save()
	messages.success(request, 'Header Color is Changed successfully')
	context={
		'hcolor':hcolor,'setcolor':'active', 'set':'active'
	}
	return redirect('/setting/headercolor')
	return render(request,context)
@login_required(login_url="/accounts/login/")
def fine(request):
	cfine=Fine.objects.all()[:1].get()
	#print(cfine)
	context={
		'set':'active','fine':'active','cfine':cfine
	}
	return render(request,"setting/fine.html", context)
@login_required(login_url="/accounts/login/")
def fineenter(request):
	cfine=Fine.objects.all()[:1].get()
	cfine.fine=request.POST['fine']
	cfine.save()
	messages.success(request, 'Fine Amount is Changed successfully')
	context={
		'set':'active','fine':'active'
	}
	return redirect('/setting/fine')
	return render(request,context)



#about
def project(request):
	context={'ab':'active', 'pro':'active'}
	return render(request, "about/project.html",context)
def developers(request):
	context={'ab':'active', 'dev':'active'}
	return render(request, "about/developers.html",context)