from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
# Create your views here.


def signupView(req):
    if req.user.is_authenticated:
        return redirect('home')

    form = SignupForm()
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "Votre compte vien d'être créé.")
            return redirect('login')
    else:
        form = SignupForm()
    context = {
        "signup_page": "active",
        "title": 'signup',
        'form': form,
    }
    return render(req, 'accounts/signup.html', context)


def loginView(req):
    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'POST':
        email_or_phone = req.POST.get('email_or_phone')
        password = req.POST.get('password')

        if "@" in email_or_phone:
            user = authenticate(req, email=email_or_phone, password=password)
        # Temporary fix of the login with phone issue
        else:
            get_user = CustomUser.objects.get(phone=email_or_phone)
            user = authenticate(req, email=get_user.email, password=password)
        # else:
        #     user = authenticate(req, phone=email_or_phone, password=password)

        if user is not None:
            login(req, user)
            if 'next' in req.POST:
                return redirect(req.POST.get('next'))

            else:
                return redirect('home')
        else:
            messages.info(req, 'Infos incorrect!')
    context = {
        "login_page": "active",
        "title": 'login'}
    return render(req, 'accounts/login.html', context)


@login_required(login_url='login')
def logoutUser(req):
    logout(req)
    return redirect('login')


@login_required(login_url='login')
def users(req):
    if not req.user.is_superuser:
        return redirect(req.META.get('HTTP_REFERER'))

    users = CustomUser.objects.all()
    ordering = ['last_name']
    context = {
        "users_page": "active",
        'title': 'users',
        'users': users,
        'ordering': ordering,
    }
    return render(req, 'accounts/users.html', context)


@ login_required(login_url='login')
def user_profile(req, pk):
    user = req.user
    profile = CustomUser.objects.get(id=pk)

    if user == profile:
        form = EditUserForm(instance=profile)
        if req.method == 'POST':
            form = EditUserForm(req.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('users')

    elif user.is_staff:
        form = AdminEditUserForm(instance=profile)
        if req.method == 'POST':
            form = AdminEditUserForm(req.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('users')
    else:
        form = None

    context = {
        "profile_page": "active",
        'title': 'user_profile',
        'profile': profile,
        'form': form,
    }
    return render(req, 'accounts/profile.html', context)


@login_required(login_url='login')
def delete_user(req, pk):
    if user.is_superuser:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        user = CustomUser.objects.filter(id=pk)
        if not user:
            return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
        user.delete()
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
