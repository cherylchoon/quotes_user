from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def index(request):
    context = {
        'regForm': RegisterForm(),
        'loginForm': LoginForm()
    }
    if 'username' in request.session:
        return redirect(reverse('quotes:quotes_index'))
    return render(request, 'login/index.html', context)

def register(request):
    if request.method == 'POST':
        regForm = RegisterForm(request.POST)
        messages.add_message(request, messages.ERROR, regForm.errors)
        if regForm.is_valid():
            response = User.objects.register(request.POST)
            request.session['username'] = request.POST['alias']
            request.session['user_id'] = response['uid']
            return redirect(reverse('quotes:quotes_index'))
        else:
            return redirect(reverse('users:user_index'))

def success(request):
    return render(request, 'login/success.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            response = User.objects.login(request.POST)
            if 'error' in response:
                messages.add_message(request, messages.ERROR, 'Username/Password does not match')
                return redirect(reverse('users:user_index'))
            else:
                request.session['username'] = response['username']
                request.session['user_id'] = response['uid']
                return redirect(reverse('quotes:quotes_index'))

def logout(request):
        request.session.clear()
        return redirect(reverse('users:user_index'))
