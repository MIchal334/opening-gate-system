import threading
from adapters.inbound.controller import app
from application.ports.inbound.frame_handler import FrameHandler
from adapters.inbound.camera_frame_handler import CameraFrameHandler
from application.ports.inbound.car_handler import CarHandler
from adapters.inbound.CNN__car_handler import CNNCarHandler
from common.cofiguration import *


def run_app_service():
    flask_thread = threading.Thread(target=__run_flask, daemon=True)
    flask_thread.start()


# def run_car_handler():
#     get_car_handler().start_cnn()

def get_frame_handler_outdoor_camera() -> FrameHandler:
    return CameraFrameHandler(__get_camera_link(OUTDOOR_CAMERA_USER,
                                                OUTDOOR_CAMERA_PASSWORD,
                                                OUTDOOR_CAMERA_IP))

# def get_frame_handler_indoor_camera() -> FrameHandler:
#     return CameraFrameHandler(__get_camera_link(INDOOR_CAMERA_USER, 
#                                                 INDOOR_CAMERA_PASSWORD, 
#                                                 INDOOR_CAMERA_IP))


def get_frame_handler_indoor_camera() -> FrameHandler:
    return CameraFrameHandler(INDOR_TEST_LINK)

def get_car_handler() -> CarHandler:
    return CNNCarHandler(CAR_REGOGNIZE_CNN_PATH)

def __run_flask():
    app.run(debug=True, port=5000, use_reloader = False)

def __get_camera_link(user, password, camera_ip):
    return f'rtsp://{user}:{password}@{camera_ip}'