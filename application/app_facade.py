import logging
import time
from application.car_recognizer_service import CarRecognizerService

logger = logging.getLogger()

def get_facade():
    return AppFacade()

class AppFacade():
    
    def __init__(self) -> None:
        pass

    def indoor_main_loop(self):
        while True:
            logger.debug('Start indor loop')
            start_time = time.time()
            time.sleep(2)
            logger.debug(f'End indor loop. Time {time.time() - start_time} s ')

    def outdoor_main_loop(self):
        while True:
            logger.debug('Start outdoor loop')
            start_time = time.time()
            time.sleep(3)
            logger.debug(f'End outdoor loop. Time {time.time() - start_time} s ')