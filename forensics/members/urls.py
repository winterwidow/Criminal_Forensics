from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main.members'),
    path('members/', views.members, name='member'),
    #path('members/details/<int:id>', views.details, name='details'),
    
]
