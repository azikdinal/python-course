from flask import Flask
app = Flask(__name__)

# Импортируем все роуты из модуля routes
import routes


# Запускаем приложение
if __name__ == "__main__":
    app.run(host="31.128.35.177", port=4000, debug=True)