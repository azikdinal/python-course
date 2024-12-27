import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

# Подключение к базе данных
connection = psycopg2.connect(
    dbname="flask",
    user="flask",
    password="flask",
    host="localhost",
    port=5432
)
cursor = connection.cursor()

# Инициализация Faker
fake = Faker()

# Функции генерации данных
def generate_users(num_users):
    roles = ["Администратор", "Аналитик", "Оператор"]
    users = []
    for _ in range(num_users):
        username = fake.user_name()
        password_hash = fake.password(length=12)
        role = random.choice(roles)
        users.append((username, password_hash, role))
    return users

def generate_regions(num_regions):
    regions = []
    for _ in range(num_regions):
        region_name = fake.state()
        description = fake.text(max_nb_chars=100)
        regions.append((region_name, description))
    return regions

def generate_network_nodes(num_nodes, region_ids):
    nodes = []
    node_types = ["Вышка", "Маршрутизатор"]
    for _ in range(num_nodes):
        region_id = random.choice(region_ids)
        location = fake.city()
        node_type = random.choice(node_types)
        bandwidth_capacity = random.uniform(100, 1000)
        nodes.append((region_id, location, node_type, bandwidth_capacity))
    return nodes

def generate_metrics(num_metrics):
    metrics = []
    for _ in range(num_metrics):
        metric_name = fake.word()
        threshold = random.uniform(0.1, 10.0)
        metrics.append((metric_name, threshold))
    return metrics

def generate_sessions(num_sessions, user_ids):
    sessions = []
    statuses = ["active", "completed"]
    for _ in range(num_sessions):
        user_id = random.choice(user_ids)
        start_time = fake.date_time_between(start_date="-1y", end_date="now")
        end_time = start_time + timedelta(hours=random.randint(1, 5))
        bandwidth_used = random.uniform(0.1, 100.0)
        packet_count = random.randint(1000, 50000)
        status = random.choice(statuses)
        sessions.append((user_id, start_time, end_time, bandwidth_used, packet_count, status))
    return sessions

def generate_events(num_events, session_ids, metric_ids):
    events = []
    severities = ["Low", "Medium", "High", "Critical"]
    for _ in range(num_events):
        session_id = random.choice(session_ids)
        metric_id = random.choice(metric_ids)
        timestamp = fake.date_time_between(start_date="-1y", end_date="now")
        severity = random.choice(severities)
        description = fake.text(max_nb_chars=200)
        events.append((session_id, metric_id, timestamp, severity, description))
    return events

# Функции вставки данных
def insert_users(users):
    query = """
        INSERT INTO users (username, password_hash, role)
        VALUES (%s, %s, %s) RETURNING user_id
    """
    user_ids = []
    for user in users:
        cursor.execute(query, user)
        user_ids.append(cursor.fetchone()[0])
    connection.commit()
    return user_ids

def insert_regions(regions):
    query = """
        INSERT INTO regions (region_name, description)
        VALUES (%s, %s) RETURNING region_id
    """
    region_ids = []
    for region in regions:
        cursor.execute(query, region)
        region_ids.append(cursor.fetchone()[0])
    connection.commit()
    return region_ids

def insert_network_nodes(nodes):
    query = """
        INSERT INTO network_nodes (region_id, location, node_type, bandwidth_capacity)
        VALUES (%s, %s, %s, %s) RETURNING node_id
    """
    node_ids = []
    for node in nodes:
        cursor.execute(query, node)
        node_ids.append(cursor.fetchone()[0])
    connection.commit()
    return node_ids

def insert_metrics(metrics):
    query = """
        INSERT INTO metrics (metric_name, threshold)
        VALUES (%s, %s) RETURNING metric_id
    """
    metric_ids = []
    for metric in metrics:
        cursor.execute(query, metric)
        metric_ids.append(cursor.fetchone()[0])
    connection.commit()
    return metric_ids

def insert_sessions(sessions):
    query = """
        INSERT INTO sessions (user_id, start_time, end_time, bandwidth_used, packet_count, status)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING session_id
    """
    session_ids = []
    for session in sessions:
        cursor.execute(query, session)
        session_ids.append(cursor.fetchone()[0])
    connection.commit()
    return session_ids

def insert_events(events):
    query = """
        INSERT INTO events (session_id, metric_id, timestamp, severity, description)
        VALUES (%s, %s, %s, %s, %s) RETURNING event_id
    """
    event_ids = []
    for event in events:
        cursor.execute(query, event)
        event_ids.append(cursor.fetchone()[0])
    connection.commit()
    return event_ids

# Вставка всех данных в БД
def insert_data():
    # Пользователи
    users = generate_users(10)
    user_ids = insert_users(users)

    # Регионы
    regions = generate_regions(5)
    region_ids = insert_regions(regions)

    # Сетевые узлы
    nodes = generate_network_nodes(10, region_ids)
    node_ids = insert_network_nodes(nodes)

    # Метрики
    metrics = generate_metrics(10)
    metric_ids = insert_metrics(metrics)

    # Сессии
    sessions = generate_sessions(15, user_ids)
    session_ids = insert_sessions(sessions)

    # События
    events = generate_events(20, session_ids, metric_ids)
    event_ids = insert_events(events)

    print("Данные успешно добавлены в базу данных.")

# Выполнение генерации данных
try:
    insert_data()
finally:
    cursor.close()
    connection.close()
