from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Account

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            request.session['user_data'] = [username, password]
            request.session.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/admin/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            displayName = form.cleaned_data.pop('displayName')
            password = make_password(form.cleaned_data.pop('password1'))
            form.cleaned_data.pop('password2')
            try:
                user = User.objects.create(**form.cleaned_data, password=password)
                account = Account.objects.create(
                    displayName=displayName,
                    user=user
                )
                user.save()
                account.save()
                return HttpResponseRedirect('/login/')
            except Exception as e:
                print(e)
                form.add_error('Could not create account')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
