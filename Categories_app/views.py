from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from Tasks_app.models import Task
from .forms import CategoryForm, CategoryEditForm
from django.contrib.auth.decorators import login_required


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', locals())


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    tasks = Task.objects.filter(category=category)
    return render(request, 'category_detail.html', locals())


@login_required(login_url='login')
def category_create(request):
    form = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Category.objects.create(name=cd['name'])
            return redirect('task_list')
    return render(request, 'category_create.html', locals())


@login_required(login_url='login')
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if category.author == request.user:
        category.delete()
        return redirect('category_list')
    return redirect('category_list')


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.POST and category.author == request.user:
        form = CategoryEditForm(request.POST or None, request.FILES or None, instance=category)
        if form.is_valid():
            category.save()
            return redirect(category.get_absolute_url())
    else:
        form = CategoryEditForm(
            initial={
                'name': category.name,
            }
        )
    return render(request, 'category_edit.html', locals())
