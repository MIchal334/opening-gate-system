import numpy
from application.ports.inbound.plate_number_reader import PlateNumberReader

class OCRPlateNumberReader(PlateNumberReader):
    def __init__(self):
        pass

    def get_plate_number(self, image: 'numpy.ndarray') -> str:
        pass