import threading
from adapters.inbound.controller import app
from application.ports.inbound.frame_handler import FrameHandler
from adapters.inbound.camera_frame_handler import CameraFrameHandler
from common.cofiguration import *


def __run_flask():
    app.run(debug=True, port=5000, use_reloader = False)

def __get_camera_link(user, password, camera_ip):
    return f'rtsp://{user}:{password}@{camera_ip}'

def run_app_service():
    flask_thread = threading.Thread(target=__run_flask, daemon=True)
    flask_thread.start()

def get_frame_handler_outdoor_camera() -> FrameHandler:
    return CameraFrameHandler(__get_camera_link(OUTDOOR_CAMERA_USER,
                                                OUTDOOR_CAMERA_PASSWORD,
                                                OUTDOOR_CAMERA_IP))

def get_frame_handler_indoor_camera() -> FrameHandler:
    return CameraFrameHandler(__get_camera_link(INDOOR_CAMERA_USER, 
                                                INDOOR_CAMERA_PASSWORD, 
                                                INDOOR_CAMERA_IP))
