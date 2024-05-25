from django import views
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('index/',views.index,name='index'),
    path('update/<int:task_id>/',views.update_task,name='update'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
]
