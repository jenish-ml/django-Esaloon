from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def categorys(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            choose = form.cleaned_data['choose']
            if Category.objects.filter(name=name, choose=choose).exists():
                form = CategoryForm()
                return render(request, 'category.html', {'form': form, 'msg': 'Category already exists'})
            else:
                Category.objects.create(name=name, choose=choose)
                return redirect('view_category')
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'form': form})

@login_required(login_url='/login')
def view_category(request):
    categories = Category.objects.all()
    return render(request, 'view_category.html', {'categories': categories})

@login_required(login_url='/login')
def edit_cat(request, id):
    category_instance = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category_instance)
        if form.is_valid():
            form.save()
            return redirect('view_category')
    else:
        form = CategoryForm(instance=category_instance)
    return render(request, 'edit_cat.html', {'form': form})

@login_required(login_url='/login')
def delete_cat(request, id):
    category_instance = get_object_or_404(Category, id=id)
    category_instance.delete()
    return redirect('view_category')
