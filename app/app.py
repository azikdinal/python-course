from flask import Flask
app = Flask(__name__)

# Импортируем все роуты из модуля routes
import routes


# Запускаем приложение
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)