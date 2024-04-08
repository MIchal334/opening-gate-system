from abc import ABC, abstractmethod
import numpy

class PlateDetectionHandler(ABC):

    @abstractmethod
    def get_plate_bb(self, image: 'numpy.ndarray') -> list:
        pass