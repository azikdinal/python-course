from faker import Faker
from db import connection

# Создаем объект Faker с русской локалью
faker = Faker('ru_RU')

# Генерация и вставка данных
for _ in range(100):  # Сгенерировать 100 записей
    name = faker.name()
    email = faker.email()
    age = faker.random_int(min=18, max=60)

    # Создаем курсор для работы с базой данных
    cursor = connection.cursor()
    try:
        # Вставка данных в таблицу
        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",
            (name, email, age)
        )
    except Exception as e:
        print(f"Ошибка при вставке данных: {e}")
    finally:
        cursor.close()  # Закрываем курсор

# Сохранение изменений
connection.commit()

print("100 записей успешно добавлены!")
