from menu.models import Category, Dish

def populate_coffee():
    # Создание категории "Кофейний лист"
    coffee_beans = Category.objects.get_or_create(name="Кофейний лист", description="Вишукані сорти кавових зерен з усього світу")[0]

    # Кофейные напитки
    coffees = [
        {"name": "Ефіопський Йоргачефф", "description": "Кава з Ефіопії з нотками квітів і ягід.", "ingredients": "Кавові зерна Йоргачефф", "price": 250.00, "image": "dishes/yirgacheffe.jpg"},
        {"name": "Колумбійська Супремо", "description": "Класична колумбійська кава з багатим смаком.", "ingredients": "Кавові зерна Колумбійська Супремо", "price": 220.00, "image": "dishes/colombian_supremo.jpg"},
        {"name": "Бразильський Сантос", "description": "М'яка кава з горіховими нотками.", "ingredients": "Кавові зерна Бразильський Сантос", "price": 200.00, "image": "dishes/brazilian_santos.jpg"},
        {"name": "Кенійська АА", "description": "Яскравий сорт із цитрусовими нотками.", "ingredients": "Кавові зерна Кенійська АА", "price": 270.00, "image": "dishes/kenya_aa.jpg"}
    ]

    # Добавление кофе в категорию
    for coffee in coffees:
        Dish.objects.get_or_create(
            name=coffee['name'],
            description=coffee['description'],
            ingredients=coffee['ingredients'],
            price=coffee['price'],
            category=coffee_beans,
            image=coffee['image'],
            is_available=True
        )

# Пункт 5: Гарячий шоколад
    chocolates = [
        {"name": "Класичний гарячий шоколад", "description": "Насичений гарячий шоколад.", "ingredients": "Темний шоколад, молоко, вершки", "price": 80.00, "image": "dishes/classic_hot_chocolate.jpg"},
        {"name": "Шоколад з маршмеллоу", "description": "Гарячий шоколад з повітряними маршмеллоу.", "ingredients": "Шоколад, молоко, маршмеллоу", "price": 90.00, "image": "dishes/hot_chocolate_marshmallow.jpg"},
        {"name": "Шоколад з апельсином", "description": "Шоколадний напій з цитрусовими нотками.", "ingredients": "Шоколад, молоко, апельсинова цедра", "price": 85.00, "image": "dishes/orange_hot_chocolate.jpg"},
        {"name": "М'ятний гарячий шоколад", "description": "Освіжаючий шоколад з м'ятою.", "ingredients": "Шоколад, молоко, м'ятний сироп", "price": 90.00, "image": "dishes/mint_hot_chocolate.jpg"}
    ]

    for chocolate in chocolates:
        Dish.objects.get_or_create(
            name=chocolate['name'],
            description=chocolate['description'],
            ingredients=chocolate['ingredients'],
            price=chocolate['price'],
            category=hot_chocolates,
            image=chocolate['image'],
            is_available=True
        )

    print("Coffee menu updated successfully!")
