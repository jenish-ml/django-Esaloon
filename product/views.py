from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddProductForm, ViewProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Login')
def add_product(request):
    form = AddProductForm(request.POST, request.FILES)
    if form.is_valid():
        c = request.session.get('ut', '')
        Product.objects.create(
            name=form.cleaned_data["name"],
            category=form.cleaned_data["category"],
            image=form.cleaned_data["image"],
            price=form.cleaned_data["price"],
            desc=form.cleaned_data["desc"],
            time=form.cleaned_data["time"],
            user=request.user,
            usertype=c
        )
        return redirect('/view_product')
    return render(request, 'freelance_addproduct.html', {'form': form})

@login_required(login_url='/Login')
def view_product(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'view_product.html', {'products': products})

@login_required(login_url='/Login')
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/view_product')
    else:
        form = AddProductForm(instance=product)
    return render(request, 'freelance_addproduct.html', {'form': form})

@login_required(login_url='/Login')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/view_product')

@login_required(login_url='/Login')
def freelance_add_product(request):
    form = AddProductForm(request.POST, request.FILES)
    if form.is_valid():
        c = request.session.get('ut', '')
        Product.objects.create(
            name=form.cleaned_data["name"],
            category=form.cleaned_data["category"],
            image=form.cleaned_data["image"],
            price=form.cleaned_data["price"],
            desc=form.cleaned_data["desc"],
            user=request.user,
            usertype=c
        )
        return redirect('/freelance_view_product')
    return render(request, 'freelance_addproduct.html', {'form': form})

@login_required(login_url='/Login')
def freelance_view_product(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'freelance_view_product.html', {'products': products})

@login_required(login_url='/Login')
def edit_freelance_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/freelance_view_product')
    else:
        form = AddProductForm(instance=product)
    return render(request, 'freelance_addproduct.html', {'form': form})

@login_required(login_url='/Login')
def delete_freelance_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/freelance_view_product')

@login_required(login_url='/Login')
def v_saloon_product(request, id):
    form = ViewProductForm(request.POST or None)
    products = Product.objects.filter(user=id)
    if form.is_valid():
        category = form.cleaned_data.get("category")
        if category:
            products = products.filter(category=category)
    return render(request, 'v_saloon_product.html', {'form': form, 'products': products})

@login_required(login_url='/Login')
def v_fw_product(request, id):
    form = ViewProductForm(request.POST or None)
    products = Product.objects.filter(user=id)
    if form.is_valid():
        category = form.cleaned_data.get("category")
        if category:
            products = products.filter(category=category)
    return render(request, 'v_fw_product.html', {'form': form, 'products': products})
