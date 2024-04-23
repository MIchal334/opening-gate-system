import logging
import time

from application.get_open_service import GateOpenService
from application.indoor_service import IndoorService
from application.outdoor_service import OutdoorService


logger = logging.getLogger()


class AppFacade():
    
    def __init__(self, 
                 outdoor_service: OutdoorService,
                 indoor_service: IndoorService,
                 gete_open_service: GateOpenService) -> None:
        self.outdoor_service = outdoor_service
        self.indoor_service = indoor_service
        self.gete_open_service = gete_open_service


    def indoor_main_loop(self):
        while True:
            if not(self.gete_open_service.is_idle_time):
                logger.info('Start indoor loop')
                start_time = time.time()
                if self.indoor_service.should_open_gate():
                    logger.info("OPEN GET BY INDOOR")
                    break
                logger.info(f'End indoor loop. Time {time.time() - start_time} s ')

    def outdoor_main_loop(self):
        while True:
            if not(self.gete_open_service.is_idle_time):
                logger.debug('Start outdoor loop')
                start_time = time.time()
                if(self.outdoor_service.should_open_gate()):
                    logger.info("OPEN GET BY OUTDOOR")
                    break
                logger.info(f'End outdoor loop. Time {time.time() - start_time} s ')