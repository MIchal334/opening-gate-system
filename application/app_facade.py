import logging
import time
from application.car_recognizer_service import CarRecognizerService, get_car_regognize_service
from application.frame_service import FrameService, get_frame_service
from application.outdoor_service import get_outdoor_service, OutdoorService

logger = logging.getLogger()

def get_facade():
    return AppFacade(get_car_regognize_service(),get_frame_service(), get_outdoor_service())

class AppFacade():
    
    def __init__(self, 
                 car_regognize_service:CarRecognizerService,
                 frame_service:FrameService,
                 outdoor_service: OutdoorService) -> None:
        self.car_regognize_service = car_regognize_service
        self.frame_service = frame_service
        self.outdoor_service = outdoor_service

    def indoor_main_loop(self):
        while True:
            logger.debug('Start indor loop')
            start_time = time.time()
            frame = self.frame_service.get_indoor_frame()
            if frame is not None:
               if self.car_regognize_service.is_car_on_image(frame):
                   logger.debug('WYKRYTO AUTO')
            logger.debug(f'End indor loop. Time {time.time() - start_time} s ')

    def outdoor_main_loop(self):
        while True:
            logger.debug('Start outdoor loop')
            start_time = time.time()
            if(self.outdoor_service.should_open_gate()):
                logger.debug('Should open gate :)')
            logger.debug(f'End outdoor loop. Time {time.time() - start_time} s ')