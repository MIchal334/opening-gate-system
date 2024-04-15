from abc import ABC, abstractmethod
import numpy

class CarBBHandler(ABC):

    @abstractmethod
    def get_car_bb(self, image: 'numpy.ndarray') -> list:
        pass