from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, TaskEditForm, TagForm, TagEditForm, CommentForm, CommentEditForm
from Categories_app.models import Category
from .models import Task, Tag, Comment
from django.contrib.auth.decorators import login_required
from functools import wraps


def is_author(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        if request.user.id == task.author.id:
            return view_func(request, *args, **kwargs)
        return redirect(task.get_absolute_url())
    return _wrapped_view


def is_author_tag(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs['pk'])
        if request.user.id == tag.author.id:
            return view_func(request, *args, **kwargs)
        return redirect(tag.get_absolute_url())
    return _wrapped_view


def is_comment_author(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        comment = Comment.objects.get(pk=kwargs['comment_pk'])
        if request.user.id == comment.author.id:
            return view_func(request, *args, **kwargs)
        return redirect(task.get_absolute_url())
    return _wrapped_view


def task_list(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(request, 'tasks_list.html', locals())


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    tags = Tag.objects.all()
    comments = Comment.objects.filter(task=task)
    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(
                author=request.user,
                task=task,
                content=cd['content'],
            )
            return redirect(task.get_absolute_url())
    return render(request, 'task_detail.html', locals())


@login_required(login_url='login')
def task_create(request):
    form = TaskForm()
    if request.POST:
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            tags = cd.get('tags')
            new_task = Task.objects.create(title=cd['title'],
                                           image=request.FILES['image'],
                                           description=cd['description'],
                                           deadline=cd['deadline'],
                                           category=cd['category'],
                                           author=request.user)
            for tag in tags.iterator():
                new_task.tags.add(tag)
            new_task.save()
            return redirect('task_list')
    return render(request, 'task_create.html', locals())


@is_author
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.POST:
        form = TaskEditForm(request.POST or None, request.FILES or None, instance=task)
        if form.is_valid():
            cd = form.cleaned_data
            tags = cd.get('tags')
            for tag in tags.iterator():
                task.tags.add(tag)
            task.save()
            return redirect(task.get_absolute_url())
    else:
        task.tags.clear()
        form = TaskEditForm(
            initial={
                'title': task.title,
                'description': task.description,
                'image': task.image,
                'deadline': task.deadline,
                'category': task.category,
                'tags': None,
            }
        )
    return render(request, 'task_edit.html', locals())


@is_author
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


"""TAGS"""


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', locals())


def tag_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    tasks = Task.objects.filter(tags=tag)
    return render(request, 'tag_detail.html', locals())


@login_required(login_url='login')
def tag_create(request):
    form = TagForm()
    if request.POST:
        form = TagForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Tag.objects.create(title=cd['title'])
            return redirect('tags_list_url')
    return render(request, 'tag_create.html', locals())


@is_author_tag
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect('tags_list_url')


@is_author_tag
def tag_edit(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.POST:
        form = TagEditForm(request.POST or None, instance=tag)
        if form.is_valid():
            tag.save()
            return redirect(tag.get_absolute_url())
    else:
        form = TagEditForm(
            initial={
                'title': tag.title,
            }
        )
    return render(request, 'tag_edit.html', locals())


@is_comment_author
def comment_edit(request, pk, comment_pk):
    task = Task.objects.get(pk=pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.POST:
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect(task.get_absolute_url())
    else:
        form = CommentForm(
            initial={
                'content': comment.content
            }
        )
    return render(request, 'comment_edit.html', locals())


@is_comment_author
def comment_delete(request, pk, comment_pk):
    task = Task.objects.get(pk=pk)
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect(task.get_absolute_url())
