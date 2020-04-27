from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    title = "Register"
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            Name = form.cleaned_data.get('username')
            messages.success(request, f'Account Created! You can now login')
            return redirect('login')

    else:
        form = UserRegisterForm()
        title = "Register"
    return render(request,'users/register.html',{ 'form': form },{'title': title})
    

@login_required
def profile(request):
    return render(request, 'users/profile.html')