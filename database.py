from dotenv import load_dotenv
import os
import psycopg2

# использовать .env файл
load_dotenv()

# Подключение к базе данных
connection = psycopg2.connect(
    host=os.getenv("DB_HOSTNAME"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

cursor.execute("SELECT * from users;")
cursor.fetchone()


# Закрыть соединение с БД
cursor.close()
connection.close()  