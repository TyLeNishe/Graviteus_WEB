from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm




from .forms import SignUpForm, LoginForm
from .models import UserProfile


def home(request):
    return render(request, 'home.html')

def lor(request):
    return render(request, 'lor.html')


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})

def avatar_view(request):
    if request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.avatar:
        profile = request.user.userprofile
        return HttpResponse(profile.avatar, content_type=profile.avatar_content_type)
    return HttpResponse(status=404)

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    is_social_user = request.user.social_auth.exists()
    
    if request.method == 'POST' and 'avatar' in request.FILES:
        avatar_file = request.FILES['avatar']
        user_profile.avatar = avatar_file.read()
        user_profile.avatar_content_type = avatar_file.content_type
        user_profile.save()
        return redirect('profile')
    
    return render(request, 'Profile.html', {
        'user_profile': user_profile,
        'is_social_user': is_social_user
    })

@login_required
def update_email(request):
    if request.user.social_auth.exists():
        messages.error(request, 'Изменение почты недоступно для социальных аккаунтов.')
        return redirect('profile')
    
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
    

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Register.html', {'form': form})