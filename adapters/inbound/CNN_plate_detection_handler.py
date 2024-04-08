import numpy
from application.ports.inbound.plate_detection_handler import PlateDetectionHandler

class CNNPlateDetectionHandler(PlateDetectionHandler):
    def __init__(self):
        pass

    def get_plate_bb(self, image: 'numpy.ndarray') -> list:
        pass