from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddCosmeticsForm, ViewProductForm
from .models import Cosmetics
from category.models import Category

@login_required(login_url='/login')
def add_cosmetics(request):
    if request.method == 'POST':
        form = AddCosmeticsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/view_cosmetics')
    else:
        form = AddCosmeticsForm()

    return render(request, 'addproduct.html', {'form': form})

@login_required(login_url='/login')
def view_cosmetics(request):
    products = Cosmetics.objects.filter(user=request.user)
    return render(request, 'view_cosmetics.html', {'products': products})

@login_required(login_url='/login')
def edit_cosmetics(request, id):
    product = get_object_or_404(Cosmetics, id=id)

    if request.method == 'POST':
        form = AddCosmeticsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/view_cosmetics')
    else:
        form = AddCosmeticsForm(instance=product)

    return render(request, 'edit_cosmetics.html', {'form': form})

@login_required(login_url='/login')
def delete_cosmetics(request, id):
    product = get_object_or_404(Cosmetics, id=id)
    product.delete()
    return redirect('/view_cosmetics')

@login_required(login_url='/login')
def v_saloon_cosmetics(request):
    form = ViewProductForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        selected_category = form.cleaned_data.get("category")
        if selected_category:
            products = Cosmetics.objects.filter(category=selected_category)
        else:
            products = Cosmetics.objects.all()
        return render(request, 'v_saloon_cosmetics.html', {'form': form, 'products': products})

    return render(request, 'v_saloon_cosmetics.html', {'form': form})

@login_required(login_url='/login')
def v_category_cosmetics(request):
    all_categories = Category.objects.filter(choose='cs')

    if request.method == 'POST':
        form = ViewProductForm(request.POST or None)
        if form.is_valid():
            selected_category = form.cleaned_data.get("category")
            if selected_category:
                filtered_products = Cosmetics.objects.filter(category=selected_category)
            else:
                filtered_products = Cosmetics.objects.all()
            return render(request, 'v_saloon_cosmetics.html', {'form': form, 'products': filtered_products, 'all_categories': all_categories})

    else:
        form = ViewProductForm()

    return render(request, 'vw_categories.html', {'form': form, 'all_categories': all_categories})

@login_required(login_url='/login')
def v_cosmetics(request, id):
    form = ViewProductForm(request.POST or None)
    products = None

    if request.method == 'POST' and form.is_valid():
        selected_category = form.cleaned_data.get("category")
        if selected_category:
            products = Cosmetics.objects.filter(category=selected_category).exclude(number_of_products=0)
    else:
        products = Cosmetics.objects.filter(category_id=id).exclude(number_of_products=0)

    return render(request, 'vw_cat_cos.html', {'form': form, 'products': products})
