from abc import ABC, abstractmethod
import numpy

class CarHandler(ABC):

    @abstractmethod
    def chek_if_car_on_image(self, image: 'numpy.ndarray') -> bool:
        pass