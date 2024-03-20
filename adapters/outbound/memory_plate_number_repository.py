import logging

from application.ports.outbound.plate_data_repo import PlateNumberRepository
from typing import List

logger = logging.getLogger()

class MemoryPlateNumberRepository(PlateNumberRepository):
    plate_list = []        
    
    def get_all_plate_number(self) -> List[str]:
        logger.info(f'Get plate list : {self.plate_list}')
        return self.plate_list

    def update_plate_number(self,plate_number_list: List[str]) -> None:
        logger.info(f'Save new plate list: {plate_number_list}')
        self.clear_all()
        self.plate_list.extend(plate_number_list)

    def clear_all(self) -> None:
        self.plate_list.clear()