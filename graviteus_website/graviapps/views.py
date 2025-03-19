from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib import messages
from django.core.exceptions import ValidationError

from .forms import SignUpForm, LoginForm
from .models import UserProfile


def home(request):
    return render(request, 'home.html')


def Shop(request):
    return render(request, "shop.html")

def about(request):
    return render(request, 'about.html')

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'SignUp.html', {'form': form})


def LogIn(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'LogIn.html', {'form': form})


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST' and 'avatar' in request.FILES:
        avatar_file = request.FILES['avatar']
        user_profile.avatar = avatar_file.read()
        user_profile.avatar_content_type = avatar_file.content_type
        user_profile.save()
        return redirect('profile')

    return render(request, 'Profile.html', {'user_profile': user_profile})


@login_required
def update_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('email')
        try:
            validate_email(new_email)
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Почта успешно изменена.')
        except ValidationError:
            messages.error(request, 'Некорректный адрес электронной почты.')
    return redirect('profile')


@login_required
def update_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('username', '').strip()
        if new_username:
            if User.objects.filter(username=new_username).exists():
                messages.error(request, 'Это имя пользователя уже занято.')
            else:
                user = request.user
                user.username = new_username
                user.save()
                messages.success(request, 'Имя успешно изменено.')
        else:
            messages.error(request, 'Имя пользователя не может быть пустым.')
    return redirect('profile')


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('home')
    else:
        from django.http import HttpResponseNotAllowed
        return HttpResponseNotAllowed(['POST'])