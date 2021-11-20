from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('tags/create/', views.tag_create, name='tag_create'),
    path('tags/<int:pk>/', views.tag_detail, name='tag_detail_url'),
    path('tags/<int:pk>/edit/', views.tag_edit, name='tag_edit'),
    path('tags/<int:pk>/delete/', views.tag_delete, name='tag_delete'),
    path('<int:pk>/comment_edit/<int:comment_pk>/', views.comment_edit, name='comment_edit'),
    path('<int:pk>/comment_delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
]
