from menu.models import Category, Dish

def populate_bar():
    # Категорії
    popular_drinks = Category.objects.get_or_create(name="Найпопулярніші напої світу (безалкогольні)", description="Популярні напої, які люблять у всьому світі")[0]
    non_alcoholic_cocktails = Category.objects.get_or_create(name="Безалкогольні коктейлі", description="Освіжаючі безалкогольні коктейлі")[0]

    # Найпопулярніші напої світу
    drinks = [
        {"name": "Вода", "description": "Чиста мінеральна вода.", "ingredients": "Вода", "price": 20.00, "image": "dishes/water.jpg"},
        {"name": "Чай", "description": "Класичний чорний чай.", "ingredients": "Чайні листя, вода", "price": 30.00, "image": "dishes/tea.jpg"},
        {"name": "Кава", "description": "Ароматна чорна кава.", "ingredients": "Кавові зерна, вода", "price": 50.00, "image": "dishes/coffee.jpg"},
        {"name": "Апельсиновий сік", "description": "Свіжовичавлений сік апельсина.", "ingredients": "Апельсини", "price": 70.00, "image": "dishes/orange_juice.jpg"},
        {"name": "Яблучний сік", "description": "Свіжовичавлений яблучний сік.", "ingredients": "Яблука", "price": 60.00, "image": "dishes/apple_juice.jpg"},
        {"name": "Смузі з манго", "description": "Тропічний смузі з манго.", "ingredients": "Манго, молоко, мед", "price": 80.00, "image": "dishes/mango_smoothie.jpg"},
        {"name": "Какао", "description": "Гаряче какао з молоком.", "ingredients": "Какао, молоко, цукор", "price": 40.00, "image": "dishes/cocoa.jpg"},
        {"name": "Молочний коктейль", "description": "Класичний молочний коктейль з ваніллю.", "ingredients": "Молоко, ваніль, цукор", "price": 70.00, "image": "dishes/milkshake.jpg"},
        {"name": "Зелений чай", "description": "Корисний зелений чай.", "ingredients": "Зелене чайне листя, вода", "price": 35.00, "image": "dishes/green_tea.jpg"},
        {"name": "Лимонад", "description": "Домашній лимонад з м'ятою.", "ingredients": "Лимон, вода, м'ята, цукор", "price": 50.00, "image": "dishes/lemonade.jpg"}
    ]

    for drink in drinks:
        Dish.objects.get_or_create(
            name=drink['name'],
            description=drink['description'],
            ingredients=drink['ingredients'],
            price=drink['price'],
            category=popular_drinks,
            image=drink['image'],
            is_available=True
        )

    # Безалкогольні коктейлі
    cocktails = [
        {"name": "Вірджин Мохіто", "description": "Безалкогольний мохіто з лаймом і м'ятою.", "ingredients": "Лайм, м'ята, газована вода, цукор", "price": 90.00, "image": "dishes/virgin_mojito.jpg"},
        {"name": "Піна Колада", "description": "Кокосовий коктейль з ананасом.", "ingredients": "Кокосове молоко, ананасовий сік, вершки", "price": 110.00, "image": "dishes/pina_colada.jpg"},
        {"name": "Шірлі Темпл", "description": "Освіжаючий коктейль з імбирним елем.", "ingredients": "Імбирний ель, гранатовий сироп", "price": 85.00, "image": "dishes/shirley_temple.jpg"},
        {"name": "Санрайз", "description": "Тропічний коктейль з апельсиновим соком і гренадіном.", "ingredients": "Апельсиновий сік, гренадін", "price": 100.00, "image": "dishes/sunrise.jpg"},
        {"name": "Мангова маракуя", "description": "Смузі з манго і маракуї.", "ingredients": "Манго, маракуя, лід", "price": 120.00, "image": "dishes/mango_passion.jpg"},
        {"name": "Червоний Грейпфрут", "description": "Напій з соком червоного грейпфрута.", "ingredients": "Грейпфрут, газована вода", "price": 90.00, "image": "dishes/red_grapefruit.jpg"},
        {"name": "Безалкогольний Пунш", "description": "Фруктовий пунш із льодом.", "ingredients": "Фруктовий сік, ягоди, лід", "price": 95.00, "image": "dishes/non_alcoholic_punch.jpg"},
        {"name": "Крижані ягоди", "description": "Коктейль із замороженими ягодами.", "ingredients": "Ягоди, лід, вода", "price": 80.00, "image": "dishes/icy_berries.jpg"},
        {"name": "Лаймовий сплеск", "description": "Коктейль із лаймовим соком і содою.", "ingredients": "Лайм, сода, цукор", "price": 75.00, "image": "dishes/lime_splash.jpg"},
        {"name": "Полуничний смузі", "description": "Смузі з полуницею і бананом.", "ingredients": "Полуниця, банан, молоко", "price": 85.00, "image": "dishes/strawberry_smoothie.jpg"}
    ]

    for cocktail in cocktails:
        Dish.objects.get_or_create(
            name=cocktail['name'],
            description=cocktail['description'],
            ingredients=cocktail['ingredients'],
            price=cocktail['price'],
            category=non_alcoholic_cocktails,
            image=cocktail['image'],
            is_available=True
        )

    print("Bar menu updated successfully!")
