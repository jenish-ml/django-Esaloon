from django.shortcuts import render, redirect
from .models import Registration
from category.models import Category
from .forms import RegisterForm, SaloonRegisterForm, FreelancerRegisterForm, ForgotForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import secrets

def index(request):
    obj = Registration.objects.all()
    is_logged_in = request.user.is_authenticated
    categories = Category.objects.all()
    saloons = Registration.objects.filter(usertype="2")
    freelancers = Registration.objects.filter(usertype="3")
    return render(request, 'index.html', {
        'data': obj,
        'lgn': is_logged_in,
        'cat': categories,
        'sal': saloons,
        'fr': freelancers
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if Registration.objects.filter(username=username, email=email, is_active=True).exists():
                return render(request, 'index.html', {'j': True})
            else:
                Registration.objects.create_user(
                    username=username,
                    password=form.cleaned_data["password"],
                    email=email,
                    street_name=form.cleaned_data["street_name"],
                    locality=form.cleaned_data["locality"],
                    landmark=form.cleaned_data["landmark"],
                    phone_number=form.cleaned_data["phone_no"],
                    usertype="0"
                )
                return render(request, 'login.html', {'form': form, 'log': True})
    else:
        form = RegisterForm()
    return render(request, 'reg.html', {'form': form})

def saloonreg(request):
    if request.method == 'POST':
        form = SaloonRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if Registration.objects.filter(username=username, email=email, is_active=False).exists():
                return render(request, 'index.html', {'j': True})
            else:
                Registration.objects.create_user(
                    username=username,
                    password=form.cleaned_data["password"],
                    email=email,
                    street_name=form.cleaned_data["street_name"],
                    locality=form.cleaned_data["locality"],
                    landmark=form.cleaned_data["landmark"],
                    phone_number=form.cleaned_data["phone_no"],
                    saloon_certificate=form.cleaned_data["saloon_certificate"],
                    owner=form.cleaned_data["owner"],
                    number_of_seats=form.cleaned_data["no_of_seats"],
                    status="not accepted",
                    usertype="2",
                    is_active=False
                )
                return render(request, 'login.html', {'form': form, 'login': True})
    else:
        form = SaloonRegisterForm()
    return render(request, 'reg.html', {'form': form})

def workerreg(request):
    if request.method == 'POST':
        form = FreelancerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if Registration.objects.filter(username=username, email=email, is_active=False).exists():
                return render(request, 'index.html', {'j': True})
            else:
                Registration.objects.create_user(
                    username=username,
                    password=form.cleaned_data["password"],
                    email=email,
                    street_name=form.cleaned_data["street_name"],
                    locality=form.cleaned_data["locality"],
                    landmark=form.cleaned_data["landmark"],
                    phone_number=form.cleaned_data["phone_no"],
                    experience_certificate=form.cleaned_data["experience_certificate"],
                    usertype="3",
                    is_active=False
                )
                return render(request, 'login.html', {'form': form, 'login': True})
    else:
        form = FreelancerRegisterForm()
    return render(request, 'reg.html', {'form': form})

def cos_reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if Registration.objects.filter(username=username, email=email, is_active=True).exists():
                return render(request, 'index.html', {'j': True})
            else:
                Registration.objects.create_user(
                    username=username,
                    password=form.cleaned_data["password"],
                    email=email,
                    street_name=form.cleaned_data["street_name"],
                    locality=form.cleaned_data["locality"],
                    landmark=form.cleaned_data["landmark"],
                    phone_number=form.cleaned_data["phone_no"],
                    usertype="4",
                    is_active=False
                )
                return render(request, 'login.html', {'form': form, 'login': True})
    else:
        form = RegisterForm()
    return render(request, 'reg.html', {'form': form})

def forgot_password(request):
    if request.method == "POST":
        form = ForgotForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = Registration.objects.get(email=email)
                password = secrets.token_urlsafe(6)
                subject = 'YOUR NEW PASSWORD'
                message = f'Your new password is: {password}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail(subject, message, email_from, recipient_list)
                
                user.set_password(password)
                user.save()
                form = LoginForm()
                return render(request, 'index.html', {'o': True, 'form': form})
            except Registration.DoesNotExist:
                return render(request, 'index.html', {'n': True})
    else:
        form = ForgotForm()
    return render(request, 'forgot_password.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            request.session['ut'] = user.usertype
            request.session['userid'] = user.id
            return redirect('/')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'m': True, 'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def Logout(request):
    auth_logout(request)
    return redirect('/')
