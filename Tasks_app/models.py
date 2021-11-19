from django.db import models
from django.urls import reverse
from Categories_app.models import Category
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tasks_images')
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='tasks')
    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='tasks', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[self.pk])


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='tags', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'pk': self.pk})
