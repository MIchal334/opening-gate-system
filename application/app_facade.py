import logging
import time
from application.car_recognizer_service import CarRecognizerService, get_car_regognize_service
from application.frame_service import FrameService, get_frame_service

logger = logging.getLogger()

def get_facade():
    return AppFacade(get_car_regognize_service(),get_frame_service())

class AppFacade():
    
    def __init__(self, car_regognize_service:CarRecognizerService, frame_service:FrameService) -> None:
        self.car_regognize_service = car_regognize_service
        self.frame_service = frame_service

    def indoor_main_loop(self):
        while True:
            logger.debug('Start indor loop')
            start_time = time.time()
            frame = self.frame_service.get_indor_frame()
            if frame is not None:
               if self.car_regognize_service.is_car_on_image(frame):
                   logger.debug('WYKRYTO AUTO')
            logger.debug(f'End indor loop. Time {time.time() - start_time} s ')

    def outdoor_main_loop(self):
        while True:
            logger.debug('Start outdoor loop')
            start_time = time.time()
            time.sleep(3)
            logger.debug(f'End outdoor loop. Time {time.time() - start_time} s ')