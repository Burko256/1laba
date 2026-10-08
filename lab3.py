# --- Каталог товарів ---
catalog = [
    {"id": 1, "name": "Ноутбук", "price": 25400.50, "qty": 5},
    {"id": 2, "name": "Мишка", "price": 750.00, "qty": 15},
    {"id": 3, "name": "Клавіатура", "price": 1850.25, "qty": 8}
]
cart = []

fmt = lambda price: f"{price:.2f}грн"

def show_catalog():
    print("\n--- Каталог ---")
    for p in catalog:
        print(f"{p['id']}. {p['name']} — {fmt(p['price'])} (Залишок: {p['qty']})")

def show_cart():
    if not cart:
        print("\nКошик порожній.")
        return
    print("\n--- Кошик ---")
    total = 0
    for item in cart:
        subtotal = item['price'] * item['cart_qty']
        total += subtotal
        print(f"{item['name']} x {item['cart_qty']} = {fmt(subtotal)}")
    print(f"Загалом: {fmt(total)}")

while True:
    print("\n=== МІНІ-МАГАЗИН ===")
    print("1. Покупець")
    print("2. Адміністратор")
    print("0. Вихід")

    role = input("Виберіть роль: ").strip()

    if role == "1":
        while True:
            print("\n--- Меню покупця ---")
            print("1. Каталог | 2. Додати в кошик | 3. Видалити з кошика | 4. Кошик | 5. Купити | 0. Назад")
            choice = input("Виберіть дію: ").strip()

            if choice == "1":
                show_catalog()
            elif choice == "2":
                show_catalog()
                p_id = int(input("ID товару: "))
                product = next((p for p in catalog if p['id'] == p_id), None)
                if product and product['qty'] > 0:
                    qty = int(input("Кількість: "))
                    if qty <= product['qty']:
                        cart.append(
                            {"id": product['id'], "name": product['name'], "price": product['price'], "cart_qty": qty})
                        print("✅ Додано!")
                    else:
                        print("❌ Забагато на складі.")
                else:
                    print("❌ Товар не знайдено або немає в наявності.")
            elif choice == "3":
                show_cart()
                if cart:
                    p_id = int(input("ID товару для видалення з кошика: "))
                    cart[:] = [item for item in cart if item['id'] != p_id]
                    print("🗑️ Видалено з кошика.")
            elif choice == "4":
                show_cart()
            elif choice == "5":
                if not cart:
                    print("❌ Кошик порожній!")
                    continue
                # Списання з каталогу за допомогою лямбди/фільтрації
                for item in cart:
                    p = next(x for x in catalog if x['id'] == item['id'])
                    p['qty'] -= item['cart_qty']
                print("🎉 Покупку успішно оформлено!")
                cart.clear()
            elif choice == "0":
                break

    elif role == "2":
        pwd = input("Пароль (admin): ").strip()
        if pwd == "admin":
            while True:
                print("\n--- Панель адміністратора ---")
                print("1. Переглянути залишки | 0. Назад")
                if input("Виберіть дію: ").strip() == "1":
                    print("\n--- Залишки на складі ---")
                    list(map(lambda p: print(f"{p['name']} — {p['qty']} шт."), catalog))
                else:
                    break
        else:
            print("❌ Невірний пароль!")

    elif role == "0":
        print("Бувай!")
        break