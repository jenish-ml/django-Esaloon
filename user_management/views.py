from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import geopy.distance
import geocoder
from .models import Location
from public_management.models import Registration
from .forms import LocationForm
from public_management.forms import RegisterForm, SaloonRegisterForm, FreelancerRegisterForm, ForgotForm, LoginForm

@login_required(login_url='/Login')
def view_freelance_worker(request):
    workers = Registration.objects.filter(usertype="3")
    return render(request, 'view_freelance_worker.html', {'workers': workers})

@login_required(login_url='/Login')
def view_salooner(request):
    search_query = request.GET.get('search', '')
    salooners = Registration.objects.filter(usertype="2")

    if search_query:
        salooners = salooners.filter(Q(username__icontains=search_query) | Q(landmark__icontains=search_query))

    locations = Location.objects.all()
    for salooner in salooners:
        location = locations.filter(user=salooner).first()
        if location:
            salooner.location = location.route

    return render(request, 'view_salooner.html', {'salooners': salooners, 'search_query': search_query})

@login_required(login_url='/Login')
def near_by_saloon(request):
    saloons = Location.objects.filter(user__usertype="2")
    user_location = geocoder.ip('me').latlng

    for salon in saloons:
        coords_1 = (user_location[0], user_location[1])
        coords_2 = (salon.latitude, salon.longitude)
        salon.dis = geopy.distance.geodesic(coords_1, coords_2).km

    sorted_saloons = sorted(saloons, key=lambda x: x.dis)
    return render(request, 'saloon_near_me.html', {'saloons': sorted_saloons})

@login_required(login_url='/Login')
def near_by_fre(request):
    freelancers = Location.objects.filter(user__usertype="3")
    user_location = geocoder.ip('me').latlng

    for fre in freelancers:
        coords_1 = (user_location[0], user_location[1])
        coords_2 = (fre.latitude, fre.longitude)
        fre.dis = geopy.distance.geodesic(coords_1, coords_2).km

    sorted_freelancers = sorted(freelancers, key=lambda x: x.dis)
    return render(request, 'nearme.html', {'freelancers': sorted_freelancers})

@login_required(login_url='/Login')
def edit_profile(request, id):
    user = get_object_or_404(Registration, id=id)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if 'password' in form.changed_data:
                user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('profile')
    else:
        form = RegisterForm(instance=user)
    return render(request, 'edit_prof.html', {'form': form})

@login_required(login_url='/Login')
def profile(request):
    user = get_object_or_404(Registration, id=request.user.id)
    return render(request, 'profile.html', {'user': user})

@login_required(login_url='/Login')
def edit_prof(request, id):
    user = get_object_or_404(Registration, id=id)
    if request.method == 'POST':
        if user.usertype == "2":
            form = SaloonRegisterForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                if 'password' in form.changed_data:
                    user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('profile')
    else:
        form = SaloonRegisterForm(instance=user)
    return render(request, 'edit_prof.html', {'form': form})

@login_required(login_url='/Login')
def edit_prof_fre(request, id):
    user = get_object_or_404(Registration, id=id)
    if request.method == 'POST':
        if user.usertype == "3":
            form = FreelancerRegisterForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('profile')
    else:
        form = FreelancerRegisterForm(instance=user)
    return render(request, 'edit_prof.html', {'form': form})

def add_location(request):
    user_id = request.user.id
    location_obj, created = Location.objects.get_or_create(user=Registration.objects.get(id=user_id))

    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES, instance=location_obj)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = Registration.objects.get(id=user_id)
            location.save()
            return redirect('/')
    else:
        form = LocationForm(instance=location_obj)

    return render(request, 'add_location.html', {'form': form})
