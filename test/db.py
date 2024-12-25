import psycopg2

connection = psycopg2.connect(
    dbname="flask",
    user="flask",
    password="flask",
    host="localhost",
    port=5432
)
cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
               id SERIAL PRIMARY KEY,
               name VARCHAR(100),
               email VARCHAR(100),
               age INT,
               create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
               )               
               """)

connection.commit()