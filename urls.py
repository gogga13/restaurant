from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu, name='menu'),
    path('bar/', views.bar_view, name='bar'),
    path('tea/', views.tea_page, name='tea_page'),
    path('coffee/', views.coffee_page, name='coffee_page'),
]
