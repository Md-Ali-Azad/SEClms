from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
# viewsforall (CRUD)
def viewshome(request):
    return render(request,"viewsforall/index.html")