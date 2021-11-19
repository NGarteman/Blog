from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.category_detail, name='category_detail'),
    path('create/', views.category_create, name='category_create'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category_list', views.category_list, name='category_list'),
]