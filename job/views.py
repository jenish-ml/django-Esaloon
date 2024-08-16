from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Registration
from .forms import AddJobForm

@login_required(login_url='/login')
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST, request.FILES)
        if form.is_valid():
            job = Job.objects.create(
                user=request.user.registration,  # Assuming a one-to-one relation with Registration
                job_title=form.cleaned_data['job_title'],
                job_description=form.cleaned_data['job_description'],
                salary=form.cleaned_data['salary'],
            )
            job.save()
            messages.success(request, 'Job added successfully!')
            return redirect('/')
    else:
        form = AddJobForm()

    return render(request, 'add_job.html', {'form': form})

@login_required(login_url='/login')
def vw_job(request):
    user_registration = get_object_or_404(Registration, id=request.user.id)
    jobs = Job.objects.filter(user=user_registration)
    return render(request, 'vw_job.html', {'jobs': jobs})

@login_required(login_url='/login')
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    job.delete()
    messages.success(request, 'Job deleted successfully!')
    return redirect('/vw_job')

@login_required(login_url='/login')
def vw_job_fw(request):
    jobs = Job.objects.all()
    return render(request, 'vw_job_fw.html', {'jobs': jobs})
