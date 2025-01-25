from menu.models import Category, Dish

def populate_menu():
    # Категорії
    japanese = Category.objects.get_or_create(name="Японська кухня", description="Роли, рамен, лапша")[0]
    italian = Category.objects.get_or_create(name="Італійська кухня", description="Паста, піца, риба")[0]
    ukrainian = Category.objects.get_or_create(name="Українська кухня", description="Борщ, вареники, галушки")[0]
    english_breakfast = Category.objects.get_or_create(name="Англійські сніданки", description="Класичні сніданки Англії")[0]
    french_croissants = Category.objects.get_or_create(name="Французькі круасани", description="Вишукані французькі круасани")[0]
    american_fast_food = Category.objects.get_or_create(name="Американський фастфуд", description="Гамбургери, картопля фрі та інше")[0]
    premium_dishes = Category.objects.get_or_create(name="Блюда преміум класу", description="Елітні страви для справжніх гурманів")[0]

    # Японська кухня
    Dish.objects.get_or_create(
        name="Філадельфія рол",
        description="Класичні роли з сиром Філадельфія, лососем та авокадо.",
        ingredients="Сир Філадельфія, рис, лосось, авокадо, водорості норі",
        price=150.00,
        category=japanese,
        image="dishes/philadelphia_roll.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Рамен з куркою",
        description="Традиційний японський суп з куркою, локшиною та овочами.",
        ingredients="Курка, локшина, яйце, овочевий бульйон",
        price=120.00,
        category=japanese,
        image="dishes/chicken_ramen.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Лапша удон",
        description="Смажена лапша удон з овочами та соєвим соусом.",
        ingredients="Лапша удон, овочі, соєвий соус",
        price=100.00,
        category=japanese,
        image="dishes/udon_noodles.jpg",
        is_available=True
    )

    # Італійська кухня
    Dish.objects.get_or_create(
        name="Карбонара",
        description="Паста з беконом, яйцем, вершками та сиром пармезан.",
        ingredients="Спагеті, бекон, яйце, вершки, пармезан",
        price=140.00,
        category=italian,
        image="dishes/carbonara.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Маргарита",
        description="Класична італійська піца з томатним соусом, моцарелою та базиліком.",
        ingredients="Тісто, томатний соус, моцарела, базилік",
        price=180.00,
        category=italian,
        image="dishes/margherita_pizza.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Риба на грилі",
        description="Свіжа риба, приготована на грилі з лимоном і спеціями.",
        ingredients="Риба, лимон, спеції",
        price=200.00,
        category=italian,
        image="dishes/grilled_fish.jpg",
        is_available=True
    )

    # Українська кухня
    Dish.objects.get_or_create(
        name="Борщ",
        description="Традиційний український суп з буряком, капустою та м'ясом.",
        ingredients="Буряк, капуста, картопля, м'ясо, сметана",
        price=90.00,
        category=ukrainian,
        image="dishes/borsh.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Вареники з картоплею",
        description="Домашні вареники з картоплею та цибулею.",
        ingredients="Тісто, картопля, цибуля",
        price=80.00,
        category=ukrainian,
        image="dishes/vareniki_potato.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Галушки",
        description="Традиційні українські галушки з соусом.",
        ingredients="Борошно, яйце, сметана",
        price=70.00,
        category=ukrainian,
        image="dishes/galushki.jpg",
        is_available=True
    )
 # Англійські сніданки
    Dish.objects.get_or_create(
        name="Повний англійський сніданок",
        description="Смажені яйця, бекон, ковбаски, гриби, помідори та тости.",
        ingredients="Яйця, бекон, ковбаски, гриби, помідори, тости",
        price=180.00,
        category=english_breakfast,
        image="dishes/full_english_breakfast.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Вівсяна каша з ягодами",
        description="Класична вівсянка з додаванням свіжих ягід та меду.",
        ingredients="Вівсянка, ягоди, мед",
        price=90.00,
        category=english_breakfast,
        image="dishes/oatmeal_with_berries.jpg",
        is_available=True
    )

    # Французькі круасани
    Dish.objects.get_or_create(
        name="Круасан з шоколадом",
        description="Традиційний французький круасан із шоколадною начинкою.",
        ingredients="Тісто, шоколад",
        price=70.00,
        category=french_croissants,
        image="dishes/chocolate_croissant.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Круасан з мигдалем",
        description="Французький круасан із мигдалевою начинкою та пудрою.",
        ingredients="Тісто, мигдаль, цукрова пудра",
        price=75.00,
        category=french_croissants,
        image="dishes/almond_croissant.jpg",
        is_available=True
    )

    # Американський фастфуд
    Dish.objects.get_or_create(
        name="Чізбургер",
        description="Класичний американський чізбургер із соковитою котлетою та сиром.",
        ingredients="Булочка, котлета, сир, овочі, соус",
        price=120.00,
        category=american_fast_food,
        image="dishes/cheeseburger.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Картопля фрі",
        description="Хрустка картопля фрі із сіллю.",
        ingredients="Картопля, сіль, олія",
        price=50.00,
        category=american_fast_food,
        image="dishes/french_fries.jpg",
        is_available=True
    )

    # Блюда преміум класу
    Dish.objects.get_or_create(
        name="Філе міньйон",
        description="Соковите яловиче філе, приготоване до досконалості.",
        ingredients="Яловичина, спеції, соус",
        price=600.00,
        category=premium_dishes,
        image="dishes/filet_mignon.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Морожене із золотом",
        description="Ванільне морозиво, покрите їстівним золотом.",
        ingredients="Ванільне морозиво, їстівне золото",
        price=1000.00,
        category=premium_dishes,
        image="dishes/gold_ice_cream.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Фуа-гра",
        description="Делікатес із качиної печінки з соусом.",
        ingredients="Качина печінка, соус, спеції",
        price=700.00,
        category=premium_dishes,
        image="dishes/foie_gras.jpg",
        is_available=True
    )
    Dish.objects.get_or_create(
        name="Мармурова яловичина",
        description="Преміальна мармурова яловичина, смажена на грилі.",
        ingredients="Мармурова яловичина, спеції",
        price=900.00,
        category=premium_dishes,
        image="dishes/wagyu_beef.jpg",
        is_available=True
    )
    print("Menu populated successfully!")
