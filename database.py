import psycopg2

# Установление соединения с базой данных
connection = psycopg2.connect("database=flask, user=flask, password=flask")


cursor = connection.cursor()
