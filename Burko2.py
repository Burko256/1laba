
users = {
    "student1": {
        "password": "1111",
        "grades": [12, 10, 8, 11, 5, 3, 9]
    },
    "student2": {
        "password": "2222",
        "grades": [7, 6, 9, 4, 10, 12, 8]
    },
    "student3": {
        "password": "3333",
        "grades": [12, 11, 10, 9, 8, 6, 5]
    },
    "student4": {
        "password": "4444",
        "grades": [4, 3, 2, 8, 7, 10, 12]
    }
}
print("=== Система перегляду оцінок ===")

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:

    grades = users[login]["grades"]

    print("\nВхід успішний!")
    print(f"Користувач: {login}")

    print("\nВаші оцінки:")
    print(grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("\nСтатистика оцінок:")
    print(f"Кількість задовільних оцінок (5-12): {satisfactory}")
    print(f"Кількість незадовільних оцінок (1-4): {unsatisfactory}")

else:
    print("\nПомилка! Неправильний логін або пароль.")












