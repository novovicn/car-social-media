from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login 

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password1']
            #user = authenticate(username=username,password=password)
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render (request,'registration/register.html',context)            


