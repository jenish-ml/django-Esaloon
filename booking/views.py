from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.serializers import serialize
from datetime import datetime, timedelta

from .models import UserBook, Registration, Cart, Product, Cosmetics
from .forms import PaymentForm, CosPaymentForm, ReplyForm
from feedback.models import Feedbacks

@login_required(login_url='/login')
def v_today_book(request):
    today = datetime.now()
    bookings = UserBook.objects.filter(product__user=request.user, booking_date=today)
    return render(request, 'v_today_book.html', {'x': bookings})

@login_required(login_url='/login')
def payment(request, id):
    form = PaymentForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        if form.is_valid():
            user_id = request.session.get('userid')
            cart_item = Cart.objects.filter(uid=user_id).first()
            
            if cart_item:
                total_price, total_time, user_seats = process_cart_item(cart_item)
                booking_date = form.cleaned_data["booking_date"]
                booking_time = form.cleaned_data["booking_time"]
                start_time = datetime.strptime(str(booking_time), '%H:%M:%S')
                end_time = start_time + timedelta(minutes=total_time)
                overlap_count = UserBook.objects.filter(
                    booking_date=booking_date,
                    booking_time__lt=end_time,
                    end_time__gt=start_time
                ).count()
                
                if overlap_count < user_seats:
                    create_bookings_from_cart(cart_item, start_time)
                    return redirect('/my_bookings')
                else:
                    return render(request, 'ubook.html', {'form': form, 'msg': True})
            else:
                product_instance = get_object_or_404(Product, id=id)
                total_price, total_time, user_seats = process_product(product_instance)
                booking_date = form.cleaned_data["booking_date"]
                booking_time = form.cleaned_data["booking_time"]
                start_time = datetime.strptime(str(booking_time), '%H:%M:%S')
                end_time = start_time + timedelta(minutes=total_time)
                overlap_count = UserBook.objects.filter(
                    booking_date=booking_date,
                    booking_time__lt=end_time,
                    end_time__gt=start_time
                ).count()
                
                if overlap_count < user_seats:
                    create_booking_from_product(product_instance, start_time, request)
                    return redirect('/my_bookings')
                else:
                    return render(request, 'ubook.html', {'form': form, 'msg': True})
    else:
        cart_item = Cart.objects.filter(uid=request.session.get('userid')).first()
        saloon_info = None
        if cart_item:
            saloon_info = Registration.objects.get(id=cart_item.sid.user.id if cart_item.sid else cart_item.cid.user.id)
        
    return render(request, 'ubook.html', {'form': form, 's': saloon_info})

def process_cart_item(cart_item):
    total_price = 0
    total_time = 0
    user_id = cart_item.sid.user.id if cart_item.sid else cart_item.cid.user.id
    user_seats = Registration.objects.get(id=user_id).no_of_seats
    
    if cart_item.sid:
        total_price += cart_item.sid.price
        total_time += cart_item.sid.time
    else:
        total_price += cart_item.cid.price
    
    return total_price, total_time, user_seats

def create_bookings_from_cart(cart_item, start_time):
    if cart_item.sid:
        UserBook.objects.create(
            booking_date=cart_item.booking_date,
            booking_time=start_time,
            end_time=start_time + timedelta(minutes=cart_item.sid.time),
            user=cart_item.uid,
            product=cart_item.sid,
            payment="paid"
        )
        start_time += timedelta(minutes=cart_item.sid.time)
    else:
        UserBook.objects.create(
            booking_date=cart_item.booking_date,
            booking_time=start_time,
            end_time=start_time + timedelta(minutes=cart_item.cid.time),
            user=cart_item.uid,
            cosmatic_product=cart_item.cid,
            no_of_products=cart_item.no_of_products,
            payment="paid"
        )
        cart_item.cid.no_of_products -= cart_item.no_of_products
        cart_item.cid.save()
        start_time += timedelta(minutes=cart_item.cid.time)
    
    cart_item.delete()

def process_product(product_instance):
    total_price = product_instance.price
    total_time = product_instance.time
    user_id = product_instance.user.id
    user_seats = Registration.objects.get(id=user_id).no_of_seats
    return total_price, total_time, user_seats

def create_booking_from_product(product_instance, start_time, request):
    UserBook.objects.create(
        booking_date=datetime.today(),
        booking_time=start_time,
        end_time=start_time + timedelta(minutes=product_instance.time),
        user=request.user,
        product=product_instance,
        payment="paid"
    )

@login_required(login_url='/login')
def my_booking(request):
    today = datetime.today()
    past_bookings = UserBook.objects.filter(user=request.session['userid'], booking_date__lt=today)
    upcoming_bookings = UserBook.objects.filter(user=request.session['userid'], booking_date__gte=today)
    
    total_price_past = calculate_total_price(past_bookings)
    total_price_upcoming = calculate_total_price(upcoming_bookings)
    
    all_feedbacks = Feedbacks.objects.filter(rid=request.session['userid'])
    total_price = total_price_past + total_price_upcoming
    now = datetime.now()

    return render(request, 'my_booking.html', {
        'a': past_bookings,
        'b': upcoming_bookings,
        'c': all_feedbacks,
        'total_price': total_price,
        'now': now
    })

def calculate_total_price(bookings):
    total_price = 0
    for booking in bookings:
        if booking.product:
            total_price += booking.product.price
        if booking.cosmatic_product:
            total_price += booking.cosmatic_product.price * booking.no_of_products
    return total_price

def todaysBooking(request):
    date_str = request.POST['d']
    start_time_str = request.POST['s']
    end_time_str = request.POST['e']
    user_id = request.session['userid']
    user = Registration.objects.get(id=user_id)

    bookings = UserBook.objects.filter(booking_date=date_str, product__user=user)
    if start_time_str:
        bookings = bookings.filter(end_time__gte=start_time_str)
    if end_time_str:
        bookings = bookings.filter(booking_time__lte=end_time_str)
    
    bookings = bookings.order_by('booking_time')
    data = serialize("json", bookings)
    return JsonResponse({'data': data}, status=200)

@login_required(login_url='/login')
def book_all(request):
    form = PaymentForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        if form.is_valid():
            user_id = request.session['userid']
            carts = Cart.objects.filter(uid=user_id)
            total_price = 0
            total_time = 0
            for cart in carts:
                if cart.sid:
                    total_price += cart.sid.price
                    total_time += cart.sid.time
                else:
                    total_price += cart.cid.price

            user_seats = Registration.objects.get(id=user_id).no_of_seats
            booking_date = form.cleaned_data["booking_date"]
            booking_time = form.cleaned_data["booking_time"]
            start_time = datetime.strptime(str(booking_time), '%H:%M:%S')
            end_time = start_time + timedelta(minutes=total_time)

            overlapping_bookings = UserBook.objects.filter(
                booking_date=booking_date,
                booking_time__lt=end_time,
                end_time__gt=start_time
            ).count()
            
            if overlapping_bookings < user_seats:
                for cart in carts:
                    if cart.sid:
                        create_booking_from_cart_item(cart, start_time)
                    else:
                        create_cosmetic_booking(cart, start_time)
                    cart.delete()
                return redirect('/my_bookings')
            else:
                return render(request, 'ubook.html', {'form': form, 'msg': True})
    else:
        first_cart = Cart.objects.filter(uid=request.session['userid']).first()
        saloon_info = Registration.objects.get(id=first_cart.sid.user.id if first_cart.sid else first_cart.cid.user.id) if first_cart else None
        return render(request, 'ubook.html', {'form': form, 's': saloon_info})

def create_booking_from_cart_item(cart, start_time):
    UserBook.objects.create(
        booking_date=cart.booking_date,
        booking_time=start_time,
        end_time=start_time + timedelta(minutes=cart.sid.time),
        user=cart.uid,
        product=cart.sid,
        payment="paid"
    )
    start_time += timedelta(minutes=cart.sid.time)

def create_cosmetic_booking(cart, start_time):
    UserBook.objects.create(
        booking_date=cart.booking_date,
        booking_time=start_time,
        end_time=start_time + timedelta(minutes=cart.cid.time),
        user=cart.uid,
        cosmatic_product=cart.cid,
        no_of_products=cart.no_of_products,
        payment="paid"
    )
    cart.cid.no_of_products -= cart.no_of_products
    cart.cid.save()
    start_time += timedelta(minutes=cart.cid.time)

@login_required(login_url='/login')
def cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        product = Product.objects.get(id=id)
        user_id = request.session['userid']
        existing_cart_item = Cart.objects.filter(uid=user_id, cid=product).first()
        
        if existing_cart_item:
            existing_cart_item.no_of_products += quantity
            existing_cart_item.save()
        else:
            Cart.objects.create(uid=user_id, cid=product, no_of_products=quantity)
        
        return redirect('/my_cart')

    return redirect('/my_cart')

@login_required(login_url='/login')
def my_cart(request):
    cart_items = Cart.objects.filter(uid=request.session['userid'])
    return render(request, 'my_cart.html', {'carts': cart_items})

@login_required(login_url='/login')
def feedbacks(request):
    feedbacks = Feedbacks.objects.filter(rid=request.session['userid'])
    return render(request, 'feedbacks.html', {'feedbacks': feedbacks})

@login_required(login_url='/login')
def add_feedback(request):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            feedback_id = form.cleaned_data['feedback_id']
            feedback = Feedbacks.objects.get(id=feedback_id)
            feedback.reply = form.cleaned_data['reply']
            feedback.save()
            return redirect('/feedbacks')
    
    return render(request, 'add_feedback.html', {'form': ReplyForm()})
