# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm

# --- ورود ---
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید!')
                return redirect('home')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

# --- خروج ---
def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید!')
    return redirect('home')  # یا 'login'

# --- ثبت‌نام ---
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})