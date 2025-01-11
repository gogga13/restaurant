from django.shortcuts import render, get_object_or_404
from .models import Dish, Category

def home(request):
    dishes = Dish.objects.filter(is_available=True)[:10]
    return render(request, 'menu/home.html', {'dishes': dishes})



def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu.html', {'categories': categories})



def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    return render(request, 'menu/dish_detail.html', {'dish': dish})
