from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.create_visitor, name='create_visitor'),
    path('', views.retrieve_visitor, name='retrieve_visitor'),
    path('', views.retrieve_visitors, name='retrieve_visitors'),
    path('', views.update_visitor, name='update_visitors'),
    path('', views.delete_visitor, name='delete_visitors'),
    path('create_visitee/', views.create_visitee, name='create_visitee'),
    path('retrieve_visitee/', views.retrieve_visitee, name='retrieve_visitee'),
    path('retrieve_visitees/', views.retrieve_visitees, name='retrieve_visitees'),
    path('update_visitee/', views.update_visitee, name='update_visitee'),
    path('delete_visitee/', views.delete_visitee, name='delete_visitee'),
    path('create_organization/', views.create_organization, name='create_organization'),
    path('retrieve_organization/', views.retrieve_organization, name='retrieve_organization'),
    path('retrieve_organization/', views.retrieve_organizations, name='retrieve_organizations'),
    path('update_organization/', views.update_organization, name='update_organization'),
    path('delete_organization/', views.delete_organization, name='delete_organization'),
]
