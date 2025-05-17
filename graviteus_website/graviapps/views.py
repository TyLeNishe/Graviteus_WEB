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

import logging

logger = logging.getLogger('graviapps')


def home(request):
    logger.info("Home page is open")
    return render(request, 'home.html')


def lor(request):
    logger.info("Lore page is open")
    return render(request, 'lor.html')


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"User {user.username} logged in successfully.")
            return redirect('home')
        else:
            logger.warning("Login attempt failed: Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})


def avatar_view(request):
    if request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.avatar:
        profile = request.user.userprofile
        logger.info(f"Avatar for user {request.user.username} is being accessed.")
        return HttpResponse(profile.avatar, content_type=profile.avatar_content_type)
    logger.warning("Avatar access failed: User is not authenticated or has no avatar.")
    return HttpResponse(status=404)


def shop(request):
    logger.info("Shop page is open")
    return render(request, 'shop.html')


def about(request):
    logger.info("Info page is open")
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
        logger.info(f"User {request.user.username} updated their avatar.")
        return redirect('profile')

    logger.info(f"User {request.user.username} accessed their profile.")
    return render(request, 'Profile.html', {
        'user_profile': user_profile,
        'is_social_user': is_social_user
    })


@login_required
def update_email(request):
    if request.user.social_auth.exists():
        messages.error(request, 'Изменение почты недоступно для социальных аккаунтов.')
        logger.warning(f"User {request.user.username} attempted to change email but is a social user.")
        return redirect('profile')

    if request.method == 'POST':
        new_email = request.POST.get('email')
        try:
            validate_email(new_email)
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Почта успешно изменена.')
            logger.info(f"User {request.user.username} changed their email to {new_email}.")
        except ValidationError:
            messages.error(request, 'Некорректный адрес электронной почты.')
            logger.error(f"User {request.user.username} provided an invalid email: {new_email}.")
    return redirect('profile')


@login_required
def update_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('username', '').strip()
        if new_username:
            if User.objects.filter(username=new_username).exists():
                messages.error(request, 'Это имя пользователя уже занято.')
                logger.warning(
                    f"User {request.user.username} attempted to change username to {new_username}, but it is already taken.")
            else:
                user = request.user
                user.username = new_username
                user.save()
                messages.success(request, 'Имя успешно изменено.')
                logger.info(f"User {request.user.username} changed their username to {new_username}.")
        else:
            messages.error(request, 'Имя пользователя не может быть пустым.')
            logger.warning("User attempted to change username to an empty value.")
    return redirect('profile')


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        logger.info(f"User {user.username} deleted their account.")
        return redirect('home')
    return redirect('profile')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"User {user.username} registered successfully.")
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            if user is not None:
                login(request, user)
                logger.info(f"User {user.username} logged in immediately after registration.")
                return redirect('home')
        else:
            logger.warning("Registration attempt failed: Invalid form data.")
    else:
        form = CustomUserCreationForm()

    logger.info("User accessed the registration page.")
    return render(request, 'Register.html', {'form': form})
