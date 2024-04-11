import cv2
import logging
import time
from adapters.inbound import get_car_bb_handler, get_detection_car_handler
from application.frame_service import FrameService, get_frame_service
from application.ports.inbound.car_bb_handler import CarBBHandler
from application.ports.inbound.car_detenction_handler import CarHandler
from common.singleton import SingletonMeta
import numpy

logger = logging.getLogger()

def get_indoor_service():
    return IndoorService(get_detection_car_handler()
                         ,get_frame_service()
                         ,get_car_bb_handler())

class IndoorService(metaclass=SingletonMeta):
    def __init__(self, car_handler: CarHandler,
                frame_service: FrameService, 
                car_bb_handler: CarBBHandler) -> None:
        logger.info('CRATED CAR SERVICE')
        self.car_handler = car_handler
        self.frame_service  = frame_service
        self.car_bb_handler = car_bb_handler
        self.decision_steps = 4
        self.area_map = {}
        self.time_per_step = 300 # [ms]
        self.time_trashold = 2.1 * self.time_per_step * self.decision_steps
        self.trashold_for_step = 0.1
        self.trashold_for_all = 1900 # [px]
        self.min_area_value = 300 # [px]
        self.diffrent_percents_value = 0.25
        # self.inc = 0

    
        
    def should_open_gate(self) -> bool:
        frame = self.frame_service.get_indoor_frame()
       
        if(frame is not None):
            # self.inc += 1
            # cv2.imwrite(f'Klatka-{self.inc}.jpg', frame)
            if self.car_handler.check_if_car_on_image(frame):
               logger.debug("CAR DETECTED")
               car_boxes = self.car_bb_handler.get_car_bb(frame)
               return self.__anlize_frame(car_boxes)

        return False

    def __anlize_frame(self,car_boxes) -> bool:
        area =  ((car_boxes[2] - car_boxes[0])) *  ((car_boxes[3] - car_boxes[1]))
        logger.info(f' CAR AREA = {area}')
        self.__add_new_area_row(area)
        if len(self.area_map) >= self.decision_steps:
            return self.__check_is_auto_bigger()
        return False

    def __add_new_area_row(self, area):
        if area < self.min_area_value:
            return

        now = int(1000*time.time())
        if len(self.area_map) >= self.decision_steps:
            key_to_rmove = min(self.area_map)
            del self.area_map[key_to_rmove]
    
        if len(self.area_map) > 0:
            print(f'DIFFERNT : {now - min(self.area_map)}')
            if (now - min(self.area_map)) > self.time_trashold:   
                self.area_map.clear()

        self.area_map[now] = area
    
    def __check_is_auto_bigger(self) -> bool:
        sum_step = 0
        sum_all = 0
        keys = list(self.area_map.keys())
        for i in range(len(keys) - 1):
            key1 = keys[i]
            key2 = keys[i + 1]
            value1 = self.area_map[key1]
            value2 = self.area_map[key2]
            if i == 0:
                sum_all += (value1 + value2)
            else:
                sum_all += value2 

            divided = ((value2/value1) - 1) 
            sum_step += divided
        
        last_area_key = keys[-1]
        first_arae_key = keys[0]
        diffrent_percents  = (self.area_map[last_area_key] - self.area_map[first_arae_key]) / self.area_map[first_arae_key]
        avg_by_step = sum_step/(len(self.area_map) - 1) 
        avg_all = sum_all/len(self.area_map)
        print(self.area_map)
        logger.info(f'AVG BY STEP {avg_by_step}')
        logger.info(f'AVG ALL = {avg_all}')
        logger.info(f'Dffrent percents = {diffrent_percents}')

        if (avg_by_step >= self.trashold_for_step) or (avg_by_step >= -0.05 and avg_all >= self.trashold_for_all) or (diffrent_percents >= self.diffrent_percents_value):
            return True
        
        return False
