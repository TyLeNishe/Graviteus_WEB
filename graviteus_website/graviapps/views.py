import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import UserProfile

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
            logger.info("User %s logged in successfully.", user.username)
            return redirect('home')
        logger.warning("Login attempt failed: Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})


def avatar_view(request):
    if (request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and request.user.userprofile.avatar):
        profile = request.user.userprofile
        logger.info("Avatar for user %s is being accessed.", request.user.username)
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
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    is_social_user = request.user.social_auth.exists()

    if request.method == 'POST' and 'avatar' in request.FILES:
        avatar_file = request.FILES['avatar']
        user_profile.avatar = avatar_file.read()
        user_profile.avatar_content_type = avatar_file.content_type
        user_profile.save()
        logger.info("User %s updated their avatar.", request.user.username)
        return redirect('profile')

    logger.info("User %s accessed their profile.", request.user.username)
    return render(request, 'Profile.html', {
        'user_profile': user_profile,
        'is_social_user': is_social_user
    })


@login_required


def update_email(request):
    if request.user.social_auth.exists():
        messages.error(request,
                       'Изменение почты недоступно для социальных аккаунтов.')
        logger.warning("User %s attempted to change email but is a social user.",
                       request.user.username)
        return redirect('profile')

    if request.method == 'POST':
        new_email = request.POST.get('email')
        try:
            validate_email(new_email)
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Почта успешно изменена.')
            logger.info("User %s changed their email to %s.", request.user.username, new_email)
        except ValidationError:
            messages.error(request, 'Некорректный адрес электронной почты.')
            logger.error("User %s provided an invalid email: %s.", request.user.username, new_email)
    return redirect('profile')


@login_required


def update_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('username', '').strip()
        if new_username:
            if User.objects.filter(username=new_username).exists():
                messages.error(request, 'Это имя пользователя уже занято.')
                logger.warning(
                    "User %s attempted to change username to %s, but it is already taken.",
                    request.user.username, new_username
                )
            else:
                user = request.user
                user.username = new_username
                user.save()
                messages.success(request, 'Имя успешно изменено.')
                logger.info("User %s changed their username to %s.",
                            request.user.username, new_username)
        else:
            messages.error(request, 'Имя пользователя не может быть пустым.')
            logger.warning("User attempted to change username to an empty value.")
    return redirect('profile')


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        logger.info("User %s deleted their account.", user.username)
        return redirect('home')
    return redirect('profile')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info("User %s registered successfully.", user.username)
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            if user is not None:
                login(request, user)
                logger.info("User %s logged in immediately after registration.", user.username)
                return redirect('home')
        else:
            logger.warning("Registration attempt failed: Invalid form data.")
    else:
        form = CustomUserCreationForm()

    logger.info("User accessed the registration page.")
    return render(request, 'Register.html', {'form': form})
