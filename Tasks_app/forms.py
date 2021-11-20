from django import forms
from .models import Task, Tag, Comment
from Categories_app.models import Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'image', 'deadline', 'category', 'tags']


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'image', 'deadline', 'category', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('title',)


class TagEditForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('title',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
