import numpy
from common.singleton import SingletonMeta
from application.ports.inbound.plate_detection_handler import PlateDetectionHandler
from application.ports.inbound.plate_number_reader import PlateNumberReader
from application.frame_service import FrameService
from application.ports.outbound.plate_data_repo import PlateNumberRepository
import logging


logger = logging.getLogger()

class OutdoorService(metaclass=SingletonMeta):
    def __init__(self,
                plate_detect_handler: PlateDetectionHandler,
                frame_service: FrameService,
                plate_number_reader: PlateNumberReader,
                plate_repository: PlateNumberRepository) -> None:
        logger.info('CRATED OUTDOOR SERVICE')
        self.plate_detection_handler = plate_detect_handler
        self.frame_service = frame_service
        self.plate_number_reader = plate_number_reader
        self.plate_repository = plate_repository

    def should_open_gate(self) -> bool:
        frame = self.frame_service.get_outdoor_frame()
        if(frame is not None):
            plate_bounding_box = self.plate_detection_handler.get_plate_bb(frame)
            plate_image = self.__extract_plate_from_image(frame, plate_bounding_box)
            detected_plate_number = self.plate_number_reader.get_plate_number(plate_image)
            return self.__is_plate_number_authorized(detected_plate_number,self.plate_repository.get_all_plate_number())
        return False



    def __extract_plate_from_image(self, image, plate_bb) -> 'numpy.ndarray':
        pass

    def __is_plate_number_authorized(self, detected_plate_number, authorized_plate_number_set) -> bool:
        capital_authorized_plate_number_set = [s.upper() for s in authorized_plate_number_set]
        if(detected_plate_number.upper() in capital_authorized_plate_number_set):
            return True
        return False
