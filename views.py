from django.shortcuts import render, get_object_or_404
from .models import Dish, Category
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu.html', {'categories': categories})



def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    return render(request, 'menu/dish_detail.html', {'dish': dish})


def bar_page(request):
    # Получаем категории для отображения на главной странице
    bar_categories = Category.objects.filter(
        name__in=[
            "Найпопулярніші напої світу (безалкогольні)",
            "Безалкогольні коктейлі"
        ]
    )
    return render(request, 'bar.html', {'bar_categories': bar_categories})


def tea_page(request):
    tea_categories = Category.objects.filter(name="Чайний лист")
    return render(request, 'tea.html', {'tea_categories': tea_categories})

def coffee_page(request):
    # Получаем категорию кофе и горячий шоколад
    coffee_beans = Category.objects.get(name="Кофейний лист")
    hot_chocolates = Category.objects.get(name="Гарячий шоколад")
    
    # Передаем в контекст
    return render(request, 'coffee.html', {'coffee_beans': coffee_beans, 'hot_chocolates': hot_chocolates})
