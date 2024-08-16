from django.shortcuts import render, redirect, get_object_or_404
from .models import Complaints, Feedbacks
from .forms import ComplaintsForm, FeedbacksForm
from public_management.models import Registration
from booking.models import UserBook
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def add_complaints(request):
    user_id = request.user.id
    form = ComplaintsForm(request.POST, request.FILES)
    
    if form.is_valid():
        Complaints.objects.create(
            subject=form.cleaned_data["subject"],
            message=form.cleaned_data["message"],
            rid=Registration.objects.get(id=user_id)
        )
        return redirect('/')
    
    return render(request, 'add_complaints.html', {'form': form})

@login_required(login_url='/login')
def add_feedbacks(request, id):
    user_id = request.user.id
    booking = get_object_or_404(UserBook, id=id)
    form = FeedbacksForm(request.POST, request.FILES)

    if form.is_valid():
        rating = form.cleaned_data.get('rating')
        saloon_id = booking.product.user.id if booking.product else booking.cosmatic_product.user.id

        feedback_data = {
            'subject': form.cleaned_data["subject"],
            'message': form.cleaned_data["message"],
            'rid': Registration.objects.get(id=user_id),
            'booking_id': booking,
            'saloon_name': Registration.objects.get(id=saloon_id),
            'rating': rating
        }

        if booking.product:
            feedback_data['service_id'] = booking.product
        else:
            feedback_data['product_id'] = booking.cosmatic_product

        new_feedback = Feedbacks.objects.create(**feedback_data)
        booking.status = "feedback given"
        booking.f_id = new_feedback.id
        booking.save()

        return redirect('/')

    return render(request, 'add_feedback.html', {'form': form})

@login_required(login_url='/login')
def vw_comp(request):
    user_id = request.user.id
    complaints = Complaints.objects.filter(rid=user_id)
    return render(request, 'vw_comp.html', {'complaints': complaints})

@login_required(login_url='/login')
def vw_complaints(request):
    complaints = Complaints.objects.all()
    return render(request, 'vw_complaints.html', {'complaints': complaints})

@login_required(login_url='/login')
def vw_feedbacks(request):
    user_id = request.user.id
    name = get_object_or_404(Registration, id=user_id)
    all_feedbacks = Feedbacks.objects.all()
    user_feedbacks = Feedbacks.objects.filter(saloon_name__id=user_id)
    return render(request, 'vw_feedbacks.html', {'all_feedbacks': all_feedbacks, 'user_feedbacks': user_feedbacks, 'name': name})
