from flask import Flask, send_from_directory
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import os
import time
import webbrowser

app = Flask(__name__)

# Импортируем все роуты из модуля routes
# TODO чтобы проект работал, нужно раскомментировать следующую строку
# import routes

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.browser_open = False

    def on_any_event(self, event):
        if not self.browser_open:
            webbrowser.open("http://127.0.0.1:5000")
            self.browser_open = True

def start_flask():
    app.run(debug=False, use_reloader=False)

# Запускаем приложение
if __name__ == "__main__":
	threading.Thread(target=start_flask, daemon=True).start()

	event_handler = ReloadHandler()
	observer = Observer()
	observer.schedule(event_handler, '.', recursive=True)
	observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
