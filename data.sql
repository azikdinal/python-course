-- Создание таблицы пользователей
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    password_hash VARCHAR NOT NULL,
    role VARCHAR NOT NULL CHECK (role IN ('Администратор', 'Аналитик', 'Оператор')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание таблицы сессий
CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    bandwidth_used FLOAT,
    packet_count INTEGER,
    status VARCHAR NOT NULL
);

-- Создание таблицы сетевых узлов
CREATE TABLE network_nodes (
    node_id SERIAL PRIMARY KEY,
    region_id INTEGER NOT NULL REFERENCES regions(region_id),
    location VARCHAR NOT NULL,
    node_type VARCHAR NOT NULL,
    bandwidth_capacity FLOAT NOT NULL
);

-- Создание таблицы регионов
CREATE TABLE regions (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR NOT NULL,
    description TEXT
);

-- Создание таблицы типов устройств
CREATE TABLE device_types (
    device_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR NOT NULL,
    description TEXT
);

-- Создание таблицы метрик
CREATE TABLE metrics (
    metric_id SERIAL PRIMARY KEY,
    metric_name VARCHAR NOT NULL,
    threshold FLOAT NOT NULL
);

-- Создание таблицы событий
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES sessions(session_id),
    metric_id INTEGER NOT NULL REFERENCES metrics(metric_id),
    timestamp TIMESTAMP NOT NULL,
    severity VARCHAR NOT NULL,
    description TEXT
);

-- Создание таблицы статистики трафика
CREATE TABLE traffic_statistics (
    stat_id SERIAL PRIMARY KEY,
    node_id INTEGER NOT NULL REFERENCES network_nodes(node_id),
    timestamp TIMESTAMP NOT NULL,
    incoming_traffic FLOAT NOT NULL,
    outgoing_traffic FLOAT NOT NULL,
    packet_loss FLOAT,
    latency INTEGER
);

-- Создание таблицы оповещений
CREATE TABLE alerts (
    alert_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id),
    alert_type VARCHAR NOT NULL,
    alert_message TEXT NOT NULL,
    is_resolved BOOLEAN DEFAULT FALSE,
    resolved_at TIMESTAMP
);

-- Создание таблицы настроек оповещений
CREATE TABLE alert_settings (
    setting_id SERIAL PRIMARY KEY,
    metric_id INTEGER NOT NULL REFERENCES metrics(metric_id),
    threshold FLOAT NOT NULL,
    severity_level VARCHAR NOT NULL,
    enabled BOOLEAN DEFAULT TRUE
);

-- Создание таблицы логов
CREATE TABLE logs (
    log_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES sessions(session_id),
    event_id INTEGER REFERENCES events(event_id),
    timestamp TIMESTAMP NOT NULL,
    log_message TEXT NOT NULL,
    severity VARCHAR NOT NULL
);
