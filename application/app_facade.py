import logging
import time
from application.frame_service import FrameService, get_frame_service
from application.indoor_service import IndoorService, get_indoor_service
from application.outdoor_service import get_outdoor_service, OutdoorService

logger = logging.getLogger()

def get_facade():
    return AppFacade(get_outdoor_service(),get_indoor_service())

class AppFacade():
    
    def __init__(self, 
                 outdoor_service: OutdoorService,
                 indoor_service: IndoorService) -> None:
        self.outdoor_service = outdoor_service
        self.indoor_service = indoor_service


    def indoor_main_loop(self):
        while True:
            logger.info('Start indor loop')
            start_time = time.time()
            if self.indoor_service.should_open_gate():
                logger.info("OPEN GET")
                break
            logger.info(f'End indor loop. Time {time.time() - start_time} s ')

    def outdoor_main_loop(self):
        while True:
            logger.debug('Start outdoor loop')
            start_time = time.time()
            if(self.outdoor_service.should_open_gate()):
                logger.debug('Should open gate :)')
            logger.debug(f'End outdoor loop. Time {time.time() - start_time} s ')