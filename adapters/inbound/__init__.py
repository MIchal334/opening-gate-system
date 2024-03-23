import threading
from adapters.inbound.controller import app

def __run_flask():
    app.run(debug=True, port=5000, use_reloader = False)

def run_app_service():
    flask_thread = threading.Thread(target=__run_flask, daemon=True)
    flask_thread.start()
