import kink

from adapters.inbound.CNN_car_bb_handler import CNNCarBBHandler
from adapters.inbound.CNN_plate_detection_handler import CNNPlateDetectionHandler
from adapters.inbound.OCR_plate_number_reader import OCRPlateNumberReader
from adapters.inbound.camera_frame_handler import CameraFrameHandler
from adapters.inbound.rasberry_gate_oppener import RassberryGateOpenner
from adapters.outbound.memory_plate_number_repository import MemoryPlateNumberRepository
from application.app_facade import AppFacade
from application.gate_open_service import GateOpenService
from application.outdoor_service import OutdoorService
from application.ports.inbound.car_bb_handler import CarBBHandler
from application.ports.inbound.gate_oppener import GateOppener
from application.ports.inbound.plate_detection_handler import PlateDetectionHandler
from application.ports.inbound.plate_number_reader import PlateNumberReader
from application.ports.outbound.plate_data_repo import PlateNumberRepository
from common.cofiguration import *
from adapters.inbound.CNN__car_handler import CNNCarHandler
from application.frame_service import FrameService
from application.indoor_service import IndoorService
from application.ports.inbound.car_detenction_handler import CarHandler

def bootstrap_di() -> None:
    frame_handler_outdoor = CameraFrameHandler(__get_camera_link(OUTDOOR_CAMERA_USER,
                                                OUTDOOR_CAMERA_PASSWORD,
                                                OUTDOOR_CAMERA_IP))

    # frame_handler_indoor = CameraFrameHandler(__get_camera_link(INDOOR_CAMERA_USER, 
    #                                             INDOOR_CAMERA_PASSWORD, 
    #                                             INDOOR_CAMERA_IP))
    
    frame_handler_indoor = CameraFrameHandler(INDOOR_TEST_LINK)

    car_handler = CNNCarHandler(CAR_REGOGNIZE_CNN_MODEL_PATH, CAR_REGOGNIZE_CNN_FRAME_X_SIZE,CAR_REGOGNIZE_CNN_FRAME_Y_SIZE)
    kink.di[CarHandler] = car_handler

    frame_service = FrameService(frame_handler_outdoor, frame_handler_indoor)
    kink.di[FrameService] = frame_service

    car_bb_handler =CNNCarBBHandler(CAR_BB_CNN_MODEL_PATH, CAR_BB_CNN_FRAME_X_SIZE,CAR_BB_CNN_FRAME_Y_SIZE)
    kink.di[CarBBHandler] = car_bb_handler

    plate_detection_handler = CNNPlateDetectionHandler()
    kink.di[PlateDetectionHandler] = plate_detection_handler

    plate_number_reader = OCRPlateNumberReader()
    kink.di[PlateNumberReader] = plate_number_reader

    plate_number_reposiotry  = MemoryPlateNumberRepository()
    kink.di[PlateNumberRepository] = plate_number_reposiotry

    outdoor_service = OutdoorService(plate_detection_handler,frame_service, plate_number_reader,plate_number_reposiotry)
    kink.di[OutdoorService] = outdoor_service


    indoor_service = IndoorService(car_handler,frame_service,car_bb_handler)
    kink.di[IndoorService]  = indoor_service

    gate_oppener =  RassberryGateOpenner(PIN_NUMBER,OPENING_TIME)
    kink.di[GateOppener]  = gate_oppener

    gate_open_service = GateOpenService(IDLE_TIME)
    kink.di[GateOpenService] = gate_open_service


    facade = AppFacade(outdoor_service,indoor_service,gate_open_service)
    kink.di[AppFacade] = facade


def __get_camera_link(user, password, camera_ip):
    return f'rtsp://{user}:{password}@{camera_ip}'
