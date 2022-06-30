from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.create_visitor, name='create_visitor'),
    path('create_visitee/', views.create_visitee, name='create_visitee'),
    path('create_organization/', views.create_organization, name='create_organization'),
]