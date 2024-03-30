
from adapters.inbound import get_car_handler
from application.ports.inbound.car_handler import CarHandler
from common.singleton import SingletonMeta
import numpy

def get_car_regognize_service():
    return CarRecognizerService(get_car_handler())

class CarRecognizerService(metaclass=SingletonMeta):
    def __init__(self, car_handler: CarHandler) -> None:
        self.car_handler = car_handler
        
    def is_car_on_image(self, image: 'numpy.ndarray') -> bool:
        return self.car_handler.chek_if_car_on_image()