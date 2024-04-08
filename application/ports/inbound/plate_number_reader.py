from abc import ABC, abstractmethod
import numpy

class PlateNumberReader(ABC):

    @abstractmethod
    def get_plate_number(self, image: 'numpy.ndarray') -> str:
        pass