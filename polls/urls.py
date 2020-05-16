from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('getForm/', views.getForm, name='getForm'),
    path('create/', views.create, name='create'),
    path('detail/<int:question_id>', views.detail, name='detail'),

    path('getFormModelForm/', views.getFormModelForm, name='getFormModelForm'),
    path('createWithModelForm/', views.createWithModelForm, name='createWithModelForm'),
]