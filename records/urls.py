from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_visitor/', views.create_visitor, name='create_visitor'),
]