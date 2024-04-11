import threading
from adapters.inbound.CNN_car_bb_handler import CNNCarBBnHandler
from adapters.inbound.controller import app
from application.ports.inbound.car_bb_handler import CarBBHandler
from application.ports.inbound.frame_handler import FrameHandler
from adapters.inbound.camera_frame_handler import CameraFrameHandler
from application.ports.inbound.car_detenction_handler import CarHandler
from adapters.inbound.CNN__car_handler import CNNCarHandler
from application.ports.inbound.plate_detection_handler import PlateDetectionHandler
from adapters.inbound.CNN_plate_detection_handler import CNNPlateDetectionHandler
from application.ports.inbound.plate_number_reader import PlateNumberReader
from adapters.inbound.OCR_plate_number_reader import OCRPlateNumberReader
from common.cofiguration import *


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


# def get_frame_handler_indoor_camera() -> FrameHandler:
#     return CameraFrameHandler(INDOR_TEST_LINK)

def get_detection_car_handler() -> CarHandler:
    return CNNCarHandler(CAR_REGOGNIZE_CNN_MODEL_PATH, CAR_REGOGNIZE_CNN_FRAME_X_SIZE,CAR_REGOGNIZE_CNN_FRAME_Y_SIZE)


def get_car_bb_handler() -> CarBBHandler:
    return CNNCarBBnHandler(CAR_BB_CNN_MODEL_PATH, CAR_BB_CNN_FRAME_X_SIZE,CAR_BB_CNN_FRAME_Y_SIZE)


def get_plate_detection_handler() -> PlateDetectionHandler:
    return CNNPlateDetectionHandler()

def get_plate_number_reader() -> PlateNumberReader:
    return OCRPlateNumberReader()

def __run_flask():
    app.run(debug=True, port=5000, use_reloader = False)

def __get_camera_link(user, password, camera_ip):
    return f'rtsp://{user}:{password}@{camera_ip}'
