import threading
from adapters.inbound.controller import app

from common.cofiguration import *


def run_app_service():
    flask_thread = threading.Thread(target=__run_flask, daemon=True)
    flask_thread.start()


def __run_flask():
    app.run(debug=True, port=5000, use_reloader = False)