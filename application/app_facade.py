import logging
import time

from application.gate_open_service import GateOpenService
from application.indoor_service import IndoorService
from application.outdoor_service import OutdoorService


logger = logging.getLogger()


class AppFacade():
    
    def __init__(self, 
                 outdoor_service: OutdoorService,
                 indoor_service: IndoorService,
                 gate_open_service: GateOpenService) -> None:
        self.outdoor_service = outdoor_service
        self.indoor_service = indoor_service
        self.gate_open_service = gate_open_service


    def indoor_main_loop(self):
        while True:
            if not(self.gate_open_service.is_idle_time):
                logger.info('Start indoor loop')
                start_time = time.time()
                if self.indoor_service.should_open_gate():
                    logger.info("OPEN GET BY INDOOR")
                    self.gate_open_service.open_gate()
                logger.info(f'End indoor loop. Time {time.time() - start_time} s ')

    def outdoor_main_loop(self):
        while True:
            if not(self.gete_open_service.is_idle_time):
                logger.debug('Start outdoor loop')
                start_time = time.time()
                if(self.outdoor_service.should_open_gate()):
                    logger.info("OPEN GET BY OUTDOOR")
                    self.gate_open_service.open_gate()
                logger.info(f'End outdoor loop. Time {time.time() - start_time} s ')