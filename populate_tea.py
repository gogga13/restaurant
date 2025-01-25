from menu.models import Category, Dish

def populate_tea():
    # Создание категории "Чайний лист"
    tea_leaves = Category.objects.get_or_create(name="Чайний лист", description="Різноманітні сорти китайського чаю")[0]

    # Чайные напитки
    teas = [
        {"name": "Пуер", "description": "Китайський ферментований чай із насиченим смаком.", "ingredients": "Чайні листя Пуер", "price": 120.00, "image": "dishes/pu_er.jpg"},
        {"name": "Зелений чай Лунцзин", "description": "Популярний китайський зелений чай з м'яким ароматом.", "ingredients": "Чайні листя Лунцзин", "price": 150.00, "image": "dishes/longjing_tea.jpg"},
        {"name": "Улун Те Гуаньінь", "description": "Один з найкращих сортів улунів із квітковими нотками.", "ingredients": "Чайні листя Те Гуаньінь", "price": 180.00, "image": "dishes/te_guan_yin.jpg"},
        {"name": "Білий чай Бай Хао Інь Чжень", "description": "Рідкісний білий чай з ніжним смаком.", "ingredients": "Чайні листя Бай Хао Інь Чжень", "price": 200.00, "image": "dishes/bai_hao_yin_zhen.jpg"}
    ]

    # Добавление чаев в категорию
    for tea in teas:
        Dish.objects.get_or_create(
            name=tea['name'],
            description=tea['description'],
            ingredients=tea['ingredients'],
            price=tea['price'],
            category=tea_leaves,
            image=tea['image'],
            is_available=True
        )

    print("Tea menu updated successfully!")
