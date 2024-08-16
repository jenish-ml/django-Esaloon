from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from public_management.models import Registration

@login_required(login_url='/login')
def approval(request):
    registrations = Registration.objects.filter(is_active=False)
    return render(request, 'approval.html', {'registrations': registrations})

@login_required(login_url='/login')
def appro(request, id):
    registration = get_object_or_404(Registration, id=id)
    registration.is_active = True
    registration.save()

    subject = 'Account Approval'
    message = 'Your account has been approved. You can now log in and access our services.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [registration.email]

    send_mail(subject, message, email_from, recipient_list)

    return redirect('approval')

@login_required(login_url='/login')
def reject(request, id):
    registration = get_object_or_404(Registration, id=id)
    registration.is_active = False
    registration.save()

    subject = 'Account Rejection'
    message = 'Your account has been rejected. You cannot log in and access our services.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [registration.email]

    send_mail(subject, message, email_from, recipient_list)

    return redirect('approval')

@login_required(login_url='/login')
def managesaloon(request):
    saloons = Registration.objects.filter(usertype="2", is_active=True)
    return render(request, 'manage_saloon.html', {'saloons': saloons})

@login_required(login_url='/login')
def managef(request):
    decorators = Registration.objects.filter(usertype="3", is_active=True)
    return render(request, 'managef.html', {'decorators': decorators})

@login_required(login_url='/login')
def manage_seller(request):
    sellers = Registration.objects.filter(usertype="4", is_active=True)
    return render(request, 'manage_seller.html', {'sellers': sellers})

@login_required(login_url='/login')
def deletesaloon(request, id):
    registration = get_object_or_404(Registration, id=id)
    registration.delete()
    return redirect('manage_saloon')

@login_required(login_url='/login')
def deletef(request, id):
    registration = get_object_or_404(Registration, id=id)
    registration.delete()
    return redirect('managef')
