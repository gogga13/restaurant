from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),
]

